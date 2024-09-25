FROM cimg/python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "sphinx-autobuild", "-b", "dirhtml", "/docs". "/docs/html", \
	  "--re-ignore", "central-api|_build", "--host", "0.0.0.0" ]
