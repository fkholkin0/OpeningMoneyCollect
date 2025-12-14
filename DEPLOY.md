# Инструкция по развертыванию

## Подготовка к деплою

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd OpeningMoneyCollect
```

### 2. Проверка зависимостей

Убедитесь, что все внешние сервисы доступны:

- ✅ Yandex Cloud Function для авторизации Google Sheets
- ✅ Google Sheets с данными участников
- ✅ Google Apps Script webhook
- ✅ T-Bank страница сбора денег

### 3. Конфигурация окружения

Если нужно изменить URL-ы или параметры, отредактируйте:

**`paint_money_reciver.py`**:
- Строка 17: Google Sheets ID
- Строка 98: Google Apps Script URL
- Строка 99: T-Bank redirect URL

**`tadash/gsauth.py`**:
- Строка 9: Yandex Cloud Function URL
- Строка 11: Keyword для авторизации

## Варианты развертывания

### Вариант 1: Docker (Рекомендуется)

#### Локальная сборка и запуск

```bash
# Сборка образа
docker build -f base_streamlit_app.Dockerfile -t opening-money-collect .

# Запуск контейнера
docker run -d \
  --name opening-money-collect \
  -p 8501:8501 \
  opening-money-collect \
  streamlit run paint_money_reciver.py --server.port=8501 --server.address=0.0.0.0
```

Приложение будет доступно на `http://localhost:8501`

#### Docker Compose (если есть другие сервисы)

Создайте `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: base_streamlit_app.Dockerfile
    ports:
      - "8501:8501"
    command: streamlit run paint_money_reciver.py --server.port=8501 --server.address=0.0.0.0
    restart: unless-stopped
    environment:
      - PYTHONUNBUFFERED=1
```

Запуск:
```bash
docker-compose up -d
```

### Вариант 2: Прямой запуск (для разработки)

```bash
# Установка зависимостей
pipenv install

# Запуск приложения
pipenv run streamlit run paint_money_reciver.py
```

### Вариант 3: Развертывание на сервере

#### На Ubuntu/Debian сервере

```bash
# 1. Установка зависимостей системы
sudo apt update
sudo apt install -y python3.13 python3-pip python3-venv

# 2. Клонирование репозитория
git clone <repository-url>
cd OpeningMoneyCollect

# 3. Установка pipenv
pip3 install pipenv

# 4. Установка зависимостей проекта
pipenv install

# 5. Создание systemd сервиса
sudo nano /etc/systemd/system/opening-money-collect.service
```

Содержимое сервиса:

```ini
[Unit]
Description=Opening Money Collect Streamlit App
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/OpeningMoneyCollect
Environment="PATH=/path/to/OpeningMoneyCollect/.venv/bin"
ExecStart=/path/to/OpeningMoneyCollect/.venv/bin/streamlit run paint_money_reciver.py --server.port=8501 --server.address=0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# 6. Запуск сервиса
sudo systemctl daemon-reload
sudo systemctl enable opening-money-collect
sudo systemctl start opening-money-collect

# 7. Проверка статуса
sudo systemctl status opening-money-collect
```

#### Nginx reverse proxy

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Вариант 4: Cloud платформы

#### Yandex Cloud (Cloud Run / Serverless Containers)

```bash
# 1. Создание Docker образа
docker build -f base_streamlit_app.Dockerfile -t cr.yandex/<registry-id>/opening-money-collect:latest .

# 2. Push в Container Registry
docker push cr.yandex/<registry-id>/opening-money-collect:latest

# 3. Деплой через консоль или CLI
yc serverless container revision deploy \
  --container-name opening-money-collect \
  --image cr.yandex/<registry-id>/opening-money-collect:latest \
  --cores 1 \
  --memory 1GB \
  --execution-timeout 60s
```

#### VK Cloud / других провайдеров

Аналогично - сборка Docker образа и деплой в container service.

## Проверка работоспособности

После деплоя проверьте:

1. ✅ Приложение открывается в браузере
2. ✅ Загружаются данные из Google Sheets
3. ✅ Можно выбрать участников
4. ✅ Рассчитывается сумма
5. ✅ Работает отправка в Google Apps Script
6. ✅ Редирект на T-Bank работает

## Обновление приложения

### Docker

```bash
# Остановка контейнера
docker stop opening-money-collect
docker rm opening-money-collect

# Пересборка
docker build -f base_streamlit_app.Dockerfile -t opening-money-collect .

# Запуск нового контейнера
docker run -d --name opening-money-collect -p 8501:8501 opening-money-collect \
  streamlit run paint_money_reciver.py --server.port=8501 --server.address=0.0.0.0
```

### На сервере

```bash
cd OpeningMoneyCollect
git pull
pipenv install
sudo systemctl restart opening-money-collect
```

## Troubleshooting

### Проблема: Не загружаются данные из Google Sheets

Проверьте:
- Доступность Yandex Cloud Function
- Правильность keyword в `tadash/gsauth.py`
- Права доступа к Google Sheet

### Проблема: Ошибка при отправке данных

Проверьте:
- Доступность Google Apps Script URL
- Правильность формата данных

### Проблема: Не работает редирект на T-Bank

Проверьте:
- Актуальность ссылки на страницу сбора
- Открытие браузера (для локального запуска может не работать)

## Мониторинг

### Логи Docker

```bash
docker logs -f opening-money-collect
```

### Логи systemd

```bash
sudo journalctl -u opening-money-collect -f
```

## Бэкап и восстановление

### Что нужно бэкапить:

1. **Код** - уже в git репозитории
2. **Google Sheets** - автоматически сохраняется в Google
3. **Конфигурация сервера** - сохраните файлы nginx, systemd и т.д.

### Восстановление после сноса сервера:

1. Разверните новый сервер
2. Установите зависимости
3. Клонируйте репозиторий
4. Следуйте инструкциям по деплою выше
5. Убедитесь, что внешние сервисы (Yandex Cloud, Google Sheets) доступны

## CI/CD

Для автоматизации деплоя можно настроить:

- **GitHub Actions** - для сборки и деплоя Docker образа
- **GitLab CI** - аналогично
- **Yandex Cloud Functions** - для триггера обновлений

Пример `.github/workflows/deploy.yml` можно добавить позже при необходимости.

## Безопасность

⚠️ **Важно**:
- Keyword для авторизации в коде - рассмотрите вынесение в secrets
- Google Sheets ID в коде - рассмотрите использование переменных окружения
- При публичном деплое добавьте аутентификацию через Streamlit

## Контакты и поддержка

При проблемах с развертыванием проверьте:
1. Логи приложения
2. Доступность внешних сервисов
3. Версии зависимостей в Pipfile.lock
