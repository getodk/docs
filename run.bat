docker kill odk-docs
docker build -t odk-docs .
.\run-task.bat autobuild
