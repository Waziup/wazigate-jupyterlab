#!/bin/sh

if [! -d "/var/lib/waziapp/workspace"]; then
    cp /root/workspace /var/lib/waziapp
fi

cp /root/package.json /var/lib/waziapp/package.json
rm /var/lib/waziapp/proxy.sock
(cd /root/www && python /root/redirect_server.py) &
jupyter lab --ServerApp.port='9000' --ServerApp.allow_root='true' --ServerApp.token='' --ServerApp.password='' --ServerApp.allow_origin='*' --ServerApp.ip='0.0.0.0' ##--notebook-dir='/var/lib/waziapp/workspace/'