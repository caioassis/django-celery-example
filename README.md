# django-celery-example
Example project of how to setup Celery and Celery Beat to execute background and scheduled jobs. It's a simple one, 
just send users an email everyday at some hour.

> I'm assuming you're running this project in Linux, so Windows users may have to change the commands.

## Installation
This project uses Python3 and virtualenv. Install virtualenv via PIP and create an environment.
```
pip install virtualenv
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

Redis is the selected Message Queue for this example project, but others are available. I'll run Redis using Docker.
Install docker before this step.
```
docker run --name project -p 127.0.0.1:6379:6379 -d redis
```
To start Celery, execute:
```
celery -A project worker -l INFO
```
Celery Worker will start and wait for tasks.

To start Celery Beat, execute:
```
celery -A project beat -l INFO
```
