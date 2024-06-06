FROM python:3.9-bookworm

RUN apt update && apt install -y gcc

COPY ./ ./

RUN pip3 install -r requirements.txt

RUN sh proto.sh

RUN sh build.sh

CMD ["python3", "main.py"]