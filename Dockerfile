FROM python:3.12-alpine

RUN apk add --no-cache g++

COPY ./ ./

RUN pip3 install -r requirements.txt

RUN sh build.sh

CMD ["python3", "main.py"]