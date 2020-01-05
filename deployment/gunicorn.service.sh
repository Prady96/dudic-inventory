#!/bin/bash 

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=yously_rd
Group=yously_rd
WorkingDirectory=/home/yously_rd/dudic-inventory/
ExecStart=gunicorn -- 
access-logfile - --workers 3 --bind unix:/home/yously_rd/dudic-inventory/run/gunicorn.sock inventory.wsgi:application

[Install]
WantedBy=multi-user.target





















