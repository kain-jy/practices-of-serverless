FROM python:3-slim

WORKDIR /root

COPY app.py /root/app.py

RUN pip install flask

CMD ["pyhon", "app.py"]
