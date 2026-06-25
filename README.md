# University Knowledge Search System

Интеллектуальная поисковая система по внутренней базе знаний университета.

## Команда

- Backend engineer - Капранов Владимир
- Frontend engineer - Ганятов Даниял
- DevOps engineer - Сидельников Николай
- QA engineer - Халимон Иван

## Локальный запуск

### Backend

Требуется Python 3.12 и доступный PostgreSQL.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
alembic upgrade head
uvicorn backend.app.main:app --reload
```

Swagger доступен по адресу <http://127.0.0.1:8000/docs>.

### Реализовано

- FastAPI-приложение и `GET /api/v1/health`;
- `POST /api/v1/documents/upload`;
- валидация PDF/DOCX и лимита 20 МБ;
- сохранение файла с UUID в каталоге `uploads`;
- сохранение метаданных документа в PostgreSQL;
- миграция Alembic для таблицы `documents`.
