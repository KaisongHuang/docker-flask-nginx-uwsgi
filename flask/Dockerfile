# Use the Python3.7.2 image
FROM alpine:latest

RUN apk add --no-cache python3-dev && pip3 install --upgrade pip
RUN apk add nginx

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/

CMD ["/bin/bash", "docker-entrypoint.sh"]