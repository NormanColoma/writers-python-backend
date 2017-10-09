FROM phusion/baseimage
MAINTAINER Norman Coloma "ua.norman@gmail.com"
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
RUN python3 -v
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH /src
ENV ENV_CONFIG development
ENV FLASK_APP=run.py
EXPOSE 5000
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]