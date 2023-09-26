FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

# COPY app.py /app
COPY . /app

CMD ["python","app.py"]



