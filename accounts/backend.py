from accounts.models import *

import logging

class RegisterAuthBackend(object):

    def authenticate(self,email,password):
        try:
            user = Profile.objects.filter(email=email).first()
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            logging.getLogger('error_logger').error(repr(e))
            return None

    def email_verify(self,email):
        try:
            user = Profile.objects.get(email=email)
            if user.is_active:
                return user
            else:
                return None
        except Profile.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None