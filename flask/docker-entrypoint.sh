#!/bin/bash
rc-service nginx restart
uwsgi app.ini