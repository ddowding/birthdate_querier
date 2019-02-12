FROM python:3.6

COPY . /app
WORKDIR /app

# Keep the container persistently running
CMD tail -f /dev/null
