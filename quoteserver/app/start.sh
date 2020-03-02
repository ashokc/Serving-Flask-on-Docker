#!/bin/sh

HOST_DOMAIN="host.docker.internal"
HOST_IP=$(ip route | awk 'NR==1 {print $3}')
echo -e "$HOST_IP\t$HOST_DOMAIN" >> /etc/hosts
/usr/local/bin/gunicorn -c /quoteserver/config.py -b 0.0.0.0:9999 --chdir /quoteserver quotes:app


