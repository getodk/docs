#!/usr/bin/env bash

docker kill odk-docs
docker build -t odk-docs .
./run-task.sh autobuild
