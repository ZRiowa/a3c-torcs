#!/usr/bin/python3
#import docker
from a3c import A3C


if __name__ == '__main__':

#    docker_client = docker.from_env()

    a3c = A3C('docker_client', 3101, '../models/a3c/', '../logs/a3c/')
    a3c.train(2)
