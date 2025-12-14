# OpeningMoneyCollect

Streamlit приложение для сбора денег на покупку снаряжения. Дубликат проекта DataWarrior для другого домена.

## Описание

Приложение позволяет:
- Выбрать участников из Google Sheets
- Выбрать комплект снаряжения для каждого участника
- Рассчитать общую сумму к оплате
- Отправить данные в Google Apps Script
- Перенаправить на страницу оплаты T-Bank

## Технологии

- Python 3.13
- Streamlit
- Google Sheets API (через gspread)
- Pandas для работы с данными
- Yandex Cloud Functions для авторизации

## Структура проекта

```
.
├── paint_money_reciver.py      # Основное приложение
├── tadash/                      # Библиотека хелперов
│   ├── gsauth.py               # Авторизация Google Sheets
│   ├── helpers.py              # UI хелперы
│   ├── AI.py                   # AI утилиты
│   ├── colors.py               # Цветовые схемы
│   ├── filters.py              # Фильтры данных
│   └── tplotly.py              # Plotly хелперы
├── static/                      # Статические файлы
│   ├── favicon.png
│   ├── images/
│   └── fonts/
├── .streamlit/
│   └── config.toml             # Конфигурация Streamlit
├── Pipfile                      # Зависимости Python
└── base_streamlit_app.Dockerfile # Dockerfile для деплоя

```

## Важные параметры

### Google Sheets
- **Sheet ID**: `18Wf1wWZIMNCXyzAxlKtfCKfB3T9S1c2ItiBHTSOZLUI`
- **Worksheet**: `main`
- **Колонки**: A:E (FIO, status, и др.)

### Внешние сервисы
- **Yandex Cloud Function** (авторизация GSheets):
  - URL: `https://functions.yandexcloud.net/d4e2hfpc10a3unevu19o`
  - Keyword: `WZIMNCXyzAxlKtfCKfB3T9S1c2ItiBHTSO`

- **Google Apps Script** (webhook):
  - URL: `https://script.google.com/macros/s/AKfycbysTYvVhdNdu3C36psqIjQUnAdBpMM82ggamlWXSxBx70hqRhgoAT0mi4PmixVX-_xZ/exec`

- **T-Bank** (страница сбора):
  - URL: `https://www.tbank.ru/collectmoney/crowd/r_WJeJcbTXZg.FzRTyxtcnP/KIf8i73700/?short_link=6Lly6zmCwnV&httpMethod=GET`

### Комплекты и цены
- Прокатный типман: 500₽
- Механика и тубы: 1000₽
- Электроника и тубы: 1500₽

## Локальная разработка

```bash
# Установка зависимостей
pipenv install

# Запуск приложения
pipenv run streamlit run paint_money_reciver.py
```

## Деплой

См. [DEPLOY.md](DEPLOY.md)

## Зависимости

- streamlit
- pandas
- numpy
- gspread
- gspread-dataframe
- streamlit-searchbox
- pyyaml
- google-auth

## Примечания

- Проект создан как дубликат DataWarrior для другого домена
- Авторизация в Google Sheets происходит через Yandex Cloud Function
- Данные отправляются в Google Apps Script после выбора комплектов
