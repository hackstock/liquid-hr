FROM python:3.6
RUN apt-get update 
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-dev -y
ADD . /liquidhr
WORKDIR /liquidhr
RUN pip3 install --no-cache-dir -r requirements.txt
CMD gunicorn manage:app -b 0.0.0.0:5000 --workers=4 --log-level=warning