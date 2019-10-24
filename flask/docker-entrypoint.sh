#!/bin/bash
rc-service nginx restart
# cd /app
uwsgi app.ini