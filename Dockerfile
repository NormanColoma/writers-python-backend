FROM phusion/baseimage
MAINTAINER Norman Coloma "ua.norman@gmail.com"
RUN add-apt-repository ppa:jonathonf/python-3.6 && apt-get update -y \
 && apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade && python3.6 -m pip install --upgrade pip setuptools wheel
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH /src
ENV ENV_CONFIG development
ENV FLASK_APP=run.py
EXPOSE 5000
CMD [ "python3.6", "-m", "flask", "run", "--host=0.0.0.0" ]