FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8001
COPY server ./server
COPY data ./data
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8001"]
