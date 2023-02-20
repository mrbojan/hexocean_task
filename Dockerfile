FROM python:3.8

WORKDIR home/task_image_v2
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./task_image_v2 .