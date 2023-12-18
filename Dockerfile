FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=app
ENV FLASK_RUN_HOST="0.0.0.0"
ENV FLASK_RUN_PORT=8083

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "flash", "run"]

# EOF