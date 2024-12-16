FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y gcc libpq-dev

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt ./

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода проекта
COPY habit_tracker .

# Экспорт порта
EXPOSE 8000

# Команда запуска по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
