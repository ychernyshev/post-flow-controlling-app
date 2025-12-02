# Використовуємо офіційний Python образ
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Вимикаємо кешування Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Встановлюємо системні залежності (наприклад, для psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо requirements.txt
COPY requirements.txt /app/

# Встановлюємо Python-залежності
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копіюємо весь код проєкту
COPY . /app/

# Команда за замовчуванням (для dev)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
