FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install python -y python-pip python-dev build-essential
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app/app.py"]
