# Use the Python3.7.2 image
FROM alpine:latest

RUN apk add --no-cache \
python3-dev \
nginx

RUN pip3 install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install  build tools for installing uwsgi
RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers

# Install the dependencies
RUN pip install -r requirements.txt

# Delete build tools
RUN apk del .build-deps

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/

# Create dir needed to run nginx
RUN mkdir -p /run/nginx

RUN chmod +x docker-entrypoint.sh
RUN mv docker-entrypoint.sh /usr/local/bin
RUN ln -s /usr/local/bin/docker-entrypoint.sh /app
ENTRYPOINT ["docker-entrypoint.sh"]