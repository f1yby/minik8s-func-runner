FROM python:latest

RUN pip install requests

COPY main.py .
COPY main.sh .

CMD bash run.sh