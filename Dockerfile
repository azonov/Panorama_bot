FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#ENV TELEGRAM_TOKEN=
#ENV COLLECTION_ID=
#ENV TOKEN=
CMD ["python", "telegram_bot.py"]