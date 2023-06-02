# Use an official Python runtime as a parent image
FROM python:3.7-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
# RUN pip install flask flask_cors
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && pip install --no-cache-dir flask flask_cors pymongo cryptography flask_compress requests

# 设置静态文件目录
# ENV STATIC_URL /static
# ENV STATIC_PATH /app/dist/static
# COPY index.html /app/templates/
# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
