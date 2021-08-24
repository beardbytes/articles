FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip install --upgrade pip
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["web/app.py"]
EXPOSE 5000