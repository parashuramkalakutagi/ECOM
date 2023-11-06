from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from ecom import settings


class EmailTokenTemplates:

    def verify_email(user, token):
        mail_subject = 'Account Activation'
        htmly = get_template('test.html')
        data = {
            'user': user.first_name,
            'token': token,
            'domain':settings.DOMAIN,
            'protocol': 'http'
        }
        message = render_to_string('test.html', data)
        html_content = htmly.render(data)
        msg = EmailMultiAlternatives(
            mail_subject,
            message,
            "parashuramkalakutagi9@gmail.com",
            [user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def change_email(user, token, email):
        mail_subject = 'Account Activation'
        htmly = get_template('email-verification.html')
        data = {
            'user': user.first_name,
            'domain': settings.SITE_DOMAIN,
            'token': token,
            'protocol': 'https'
        }
        message = render_to_string('email-verification.html', data)
        html_content = htmly.render(data)
        msg = EmailMultiAlternatives(
            mail_subject,
            message,
            "no-reply@midchains.com",
            [email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()



