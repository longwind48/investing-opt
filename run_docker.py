"""
This file is used to generate execute docker commands

Example command:
$ python3 run_docker.py
"""

from subprocess import call
import sys

ports = '9999:8888'
cname = 'investing_opt_dev'
iname = 'investing_opt_dev_image'

input(f"Press to stop and remove old container with name {cname}")
call(f"docker stop {cname}", shell=True)
call(f"docker rm {cname}", shell=True)
print()

input(f"Press to build new image with image name {iname}")
call(f"docker build -t {iname} .", shell=True)

input(f"Press to run container with image <{iname}>, using name <{cname}>")
call(f"docker run -d -it -p {ports} --name {cname} -v $PWD:/home/jovyan/work {iname}", shell=True)

