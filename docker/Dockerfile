FROM python:3.8.5-buster

WORKDIR /rtc_docker_test_infra
ADD . /rtc_docker_test_infra


RUN pip install -r docker/config/requirements.txt

SHELL ["/bin/sh", "-c"]

RUN mkdir /tmp/results && \
    apt-get update && \
    apt-get -y install jq && \
    chmod +x docker/scripts/wait_for_selenium.sh
