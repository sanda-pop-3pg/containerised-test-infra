FROM python:3.8.5-buster

WORKDIR /containerised-test-infra
ADD . /containerised-test-infra


RUN pip install -r docker/config/requirements.txt

SHELL ["/bin/sh", "-c"]

RUN mkdir /tmp/results && \
    apt-get update && \
    apt-get -y install jq && \
    chmod +x docker/scripts/wait_for_selenium.sh
