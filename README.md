# API AI

## Overview
Данный репозиторий содержит API приложение по генирации текста с использованием GTP-2.

## Methods
- **GET** `/health/` (Возвращает status 200, если приложение OK)
- **POST** `/generate/` {'model': имя модели gpt2 или gpt2-large, 'message': текст запроса для генерации} (Возвращает status 200, {'answer': ответ модели ии})

## Quick Start (Unix)
1. Локально клонируем репозиторий проекта к себе командой:
```
git clone https://github.com/wh000ami/ai-api.git && cd ai-api
```
2. Заводим виртуальное окружение
```
python3 -m venv venv && source venv/bin/activate
```
3. Подтягиваем все зависимости
```
pip install -U requirements.txt
```
4. Запускаем локальный сервер
```
uvicorn app.controller:app --host=0.0.0.0 --port=8000 --log-level=debug --reload
```
🎉 Готово, теперь обращаясь по пути localhost:8000 мы получим результат работы.