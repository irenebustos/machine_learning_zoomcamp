# especify the base image
FROM python:3.9-slim

# install pipenv as our project uses it
RUN pip install pipenv

# create a directory in the container
WORKDIR /app

# copy the files to the container
COPY Pipfile Pipfile.lock ./

# install the dependencies. we need system and deploy to stop pipenv from creating a new virtual environment
RUN pipenv install --system --deploy  

# copy the files to the container
COPY predict.py model_C=1.0.bin ./

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]
