# Match python version to CI
FROM python:3.11

RUN apt-get update && \
    apt-get install --yes pngquant python3-enchant && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY extensions requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "sphinx-autobuild", "-b", "dirhtml", "/docs", "/docs/html", \
    "--re-ignore", "central-api|_build", "--host", "0.0.0.0" ]
