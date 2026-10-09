FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
ENV PYTHONPATH=/app:/app/main_files
WORKDIR /app/main_files