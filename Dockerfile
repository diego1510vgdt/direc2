FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /direc2
WORKDIR /direc2
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "tareas_api.py" ]