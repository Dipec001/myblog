from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from celery import shared_task

@shared_task(bind=True)
def send_normal_email(self, data):
    email = EmailMessage(
        subject=data["email_subject"],
        body=data["email_body"],
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[data["to_email"]],
    )
    email.send()