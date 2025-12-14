import requests
import json

def askMistral(data_context: str, question_context: str, selected_data: str, response_format: str = "text"):
    """
    Получает ответ от Mistral AI на основе контекста данных, вопроса,
    выбранных данных и формата ответа.

    Args:
        data_context (str): Контекст данных (например, описание продукта).
        question_context (str): Контекст вопроса (например, описание графика).
        selected_data (str): Выбранные данные (например, значения на графике).
        response_format (str): Формат ответа ("json" или "text").

    Returns:
        dict: Ответ от Mistral AI или словарь с ошибкой.
    """
    # API-ключ. Замените на ваш актуальный токен
    token = 'nUAl65wKZsaD6jd5Jg0jSum8kHBEpVZx'  # Необходимо заменить на реальный токен
    url = 'https://api.mistral.ai/v1/chat/completions'

    # Формирование текста запроса
    prompt_text = f"""
    Контекст данных: {data_context}

    Контекст вопроса: {question_context}

    Выбранные данные: {selected_data}
    """

    # Формирование тела запроса
    payload = {
        "model": "mistral-small-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    # Добавляем формат ответа, если требуется JSON
    if response_format == "json":
        payload["response_format"] = {"type": "json_object"}

    # Заголовки запроса
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    try:
        # Отправка запроса
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # Проверка HTTP-ошибок
        
        # Разбор ответа
        json_response = response.json()
        
        # Получение текста ответа
        if "choices" in json_response and len(json_response["choices"]) > 0:
            message = json_response["choices"][0].get("message", {})
            content = message.get("content", "")
            
            # Если запрошен JSON, попытаемся распарсить ответ
            if response_format == "json":
                try:
                    parsed_json = json.loads(content)
                    return {"status": 200, "data": parsed_json}
                except json.JSONDecodeError:
                    return {
                        "status": 400, 
                        "error": "API вернул некорректный JSON",
                        "raw_response": content
                    }
            else:
                return {"status": 200, "data": content}
        else:
            return {
                "status": 400, 
                "error": "Неожиданный формат ответа от API", 
                "raw_response": json_response
            }
            
    except requests.exceptions.RequestException as e:
        return {"status": 500, "error": f"Ошибка при выполнении запроса: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"status": 500, "error": f"Ошибка при разборе JSON: {str(e)}"}
    except Exception as e:
        return {"status": 500, "error": f"Непредвиденная ошибка: {str(e)}"}