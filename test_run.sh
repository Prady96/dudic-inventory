#!/bin/bash 
  
NAME="dudic-inventory"                                        # Name of the application 
DJANGODIR=/home/yously_rd/dudic-inventory/                     # Django project directory 
SOCKFILE=/home/yously_rd/dudic-inventory/run/gunicorn.sock    # we will communicte using this unix socket 
USER=yously_rd                                                # the user to run as 
GROUP=yously_rd                                               # the group to run as 
NUM_WORKERS=3                                                 # how many worker processes should Gunicorn spawn 
DJANGO_SETTINGS_MODULE=inventory.settings                     # which settings file should Django use 
DJANGO_WSGI_MODULE=inventory.wsgi                             # WSGI module name 
  
echo "Starting $NAME as `whoami`" 
  
# Activate the virtual environment 
# cd $DJANGODIR 
# Source ../venv/bin/activate
# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE 
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH 

## Documentation: https://stackoverflow.com/a/56742477/7999665
## youtube link https://youtu.be/JjwbXZwOst0
# Activate the virtual environment (virtualenv)

echo "virtualenv would be activated here `$PWD`"
# echo $PWD
activate () {
    . $PWD/venv/bin/activate
}

activate


# Create the run directory if it doesn't exist 
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR 
  
# Start your Django Unicorn 
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon) 
exec $DJANGODIR/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \ 
 --name $NAME \ 
 --workers $NUM_WORKERS \ 
 --user=$USER --group=$GROUP \ 
 --bind=$SOCKFILE \ 
 --log-level=debug \ 
 --log-file=- 




