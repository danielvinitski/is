FROM python:2.7-alpine3.9

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY customer-management.py .


CMD [ "python", "./customer-management.py" ]