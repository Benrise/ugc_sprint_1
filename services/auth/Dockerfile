FROM python:3.11-slim

WORKDIR /opt/auth

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["python3", "main.py"]