FROM python:3.10-slim
LABEL authors="abc"

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8050
CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:server"]


