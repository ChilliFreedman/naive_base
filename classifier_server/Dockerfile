FROM python:3.11-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app


RUN apt-get update && apt-get install -y gcc build-essential


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8002


CMD ["uvicorn", "classifier_server.main_classifier:app2", "--host", "0.0.0.0", "--port", "8002"]
