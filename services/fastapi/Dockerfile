FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip3.11 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]