FROM python:3-slim

WORKDIR /code

COPY app.py /code/app.py

RUN pip install flask

CMD ["pyhon", "app.py"]
