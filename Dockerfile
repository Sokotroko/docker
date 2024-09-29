FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN pip install kafka-python

CMD ["python", "producer.py"]
