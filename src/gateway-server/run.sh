#!/usr/bin/env bash
awk -F# -f bnc.awk <(echo -e $_CONF) > /etc/nginx/nginx.conf
nginx
while true; do
  sleep 1000
done
