FROM python:3.10

WORKDIR /app
COPY mqtt_issue_sample/requirements.txt .
RUN pip install -r requirements.txt

COPY mqtt_issue_sample/main_fast_api.py .
