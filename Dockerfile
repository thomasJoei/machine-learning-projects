FROM python:3.7-slim-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . /app

EXPOSE 8000

# Set code to run at container run time
ENTRYPOINT ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "bottle_app:app"]