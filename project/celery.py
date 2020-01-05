import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat configuration
# Execute task every day at 8 am. Check Celery Beat documentation for possible crontab configurations.
app.conf.beat_schedule = {
    'send_mail_task': {
        'task': 'core.tasks.notify_users',
        'schedule': crontab(minute=0, hour=8)
    }
}

# Timezone can be changed for whatever timezone you're in.
app.conf.timezone = 'Brazil/East'

app.autodiscover_tasks()
