FROM python:3.8.3-alpine3.11

COPY . /scripts
WORKDIR /scripts

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]
