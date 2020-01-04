from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


@shared_task
def notify_users():
    users = User.objects.all()
    for user in users:
        send_mail(
            'Test Subject',
            'Test Body',
            from_email='test@test.com',
            recipient_list=[user.email],
            fail_silently=False
        )
    return
