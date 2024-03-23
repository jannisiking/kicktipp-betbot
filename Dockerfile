FROM python:3.11 AS build

WORKDIR /usr/src/app

# COPY FILES
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./kicktippbb.py"]

