FROM python:3

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY links.txt /app

COPY app.py /app
CMD ["python","-u","app.py"]
