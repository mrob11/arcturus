FROM python:3.9-slim

RUN pip install 'poetry>=1.0.0'

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0"]
