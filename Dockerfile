FROM python:3

WORKDIR /mnt

VOLUME /mnt

COPY requirements.txt ./

RUN apt-get update -y && \
    apt-get install -y python3-enchant && \
    apt-get install -y --no-install-recommends texlive-xetex && \
    apt-get install -y texlive-fonts-recommended && \
	python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["make"]

EXPOSE 8080