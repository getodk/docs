#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

docker run --rm -v "${DIR}":/mnt -p 8080:8080 --name odkx-docs odkx-docs "$1"
