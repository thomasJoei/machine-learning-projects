### Start

```
# To build the image 
docker build -t ml-bootle:latest .

# To start the container
docker -d run -p 8000:8000 ml-bootle:latest


# To start the container in development mode with auto-reload and current folder binding enabled 
docker run -d \
-p 8000:8000 \
--mount type=bind,source="$(pwd)",target=/app \
--entrypoint gunicorn \
ml-bootle:latest \
--workers=2 --bind=0.0.0.0:8000 --reload bottle_app:app

```

Connect to http://127.0.0.1:8000/
On Mac, Docker do not allow connection to localhost so you need to specifically use 127.0.0.1 !