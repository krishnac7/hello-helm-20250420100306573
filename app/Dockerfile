FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask

EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]
