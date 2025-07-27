FROM python:3.11-slim


WORKDIR /app


RUN apt-get update && apt-get install -y gcc build-essential


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .
COPY ../data ./data

EXPOSE 8001


CMD ["uvicorn", "model_server.main_model:app", "--host", "0.0.0.0", "--port", "8001"]

