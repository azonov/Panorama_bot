FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV COLLECTION_ID=a37874d2-fb06-40d8-9ff4-57dbac66906b
CMD ["python", "telegram_bot.py"]