import random
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .models import *


def send_via_mail(email):
    subject = f' FORGOT PASSWORD '
    otp = random.randint(1000,9999)
    message = f'password reset  otp is {otp} '
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = Profile.objects.get(email= email)
    user_obj.mobile_otp = otp
    user_obj.save()
    return otp

class Util:
    def send_email(data):
        email = EmailMessage(subject=data['subject'],body=data['email_body'],to=[data['to_email']],from_email=settings.EMAIL_HOST)
        email.send()