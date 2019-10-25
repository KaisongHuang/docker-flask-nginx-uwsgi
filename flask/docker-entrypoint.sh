#!/bin/bash
nginx -g "daemon on;"
uwsgi app.ini