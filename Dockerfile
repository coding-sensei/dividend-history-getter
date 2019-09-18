FROM joyzoursky/python-chromedriver

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

#ENTRYPOINT /bin/bash
