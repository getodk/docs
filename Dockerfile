# consider using a non-circleci image?
# Would use cimg/python to match CI, but it does some weird stuff with users
FROM python:3.11

ARG username

RUN apt-get update && \
    apt-get install --yes pngquant python3-enchant && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY extensions requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "sphinx-autobuild", "-b", "dirhtml", "/docs", "/docs/html", \
    "--re-ignore", "central-api|_build", "--host", "0.0.0.0" ]
