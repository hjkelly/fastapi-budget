FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY gcloud-creds.json /app/
COPY app app