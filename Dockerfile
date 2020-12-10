FROM ubuntu:18.04

WORKDIR /application

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y wget tzdata

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
    chmod +x Miniconda3-latest-Linux-x86_64.sh &&\
    ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 &&\
    rm -rf ./Miniconda3-latest-Linux-x86_64.sh

COPY . .
ENV PYTHONPATH=/application

RUN /opt/miniconda3/bin/conda env create -f environment.yml -p .venv/
ENV PATH=${PATH}:/application/.venv/bin 
