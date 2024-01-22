FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY FILES
COPY . .

ENV USERNAME=""
ENV PASSWORD=""

CMD ["python", "./kicktippbb.py"]

