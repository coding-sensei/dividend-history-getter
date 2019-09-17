FROM python

RUN apt-get update && apt-get install -y sshpass

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

ENTRYPOINT /bin/bash
