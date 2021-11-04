FROM python:2.7-alpine3.9

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY customer-api-server.py .


CMD [ "python", "./customer-api-server.py" ]