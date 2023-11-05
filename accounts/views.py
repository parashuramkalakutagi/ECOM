from django.shortcuts import render
from .models import Profile
from .serializer import *
from rest_framework import viewsets
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken,BlacklistedToken
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .emails import send_via_mail,Util
from .backend import RegisterAuthBackend
import jwt
import time
from ecom import settings
import re
from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from django.urls import reverse
from django.conf import settings
from .email_templates import EmailTokenTemplates





def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def validate_args(data, args):
    for key in args:
        if key not in data.keys():
            return Response({"message": f"Invalid Arguments, required {key}", "code": 400}, status=HTTP_400_BAD_REQUEST)

    return False

def validate_email_address(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

class Profile_Register(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            auth = RegisterAuthBackend()
            number = PhoneNumber.from_string(data['mobile_number'])
            validate = validate_args(data,['email','mobile_number','first_name','last_name'])
            if validate:
                return validate

            if not number.is_valid():
                return Response({'msg':'Invalid Phone number..!','code':400},status=HTTP_400_BAD_REQUEST)

            if not validate_email_address(data['email']):
                return Response({'msg':'Invalid format email id ','code':400},status=HTTP_400_BAD_REQUEST)

            if auth.authenticate(email=data['email'],password=data['password']):
                response_data = {
                    'status_code': HTTP_400_BAD_REQUEST,
                    'message': 'email is alredy taken ....'
                }
                return Response(response_data,status=HTTP_400_BAD_REQUEST)


            else:
                if data['password'] and data['password'] == data['confirm_password']:

                    obj = Profile.objects.create(
                        email=data['email'],
                        first_name=data['first_name'],
                        last_name = data['last_name'],
                        email_verified = False
                    )
                    obj.set_password(str(data['password']))
                    obj.save()
                    user = Profile.objects.get(email=data['email'])

                    token = RefreshToken.for_user(user).access_token
                    print(token)

                    data = jwt.encode({'email':user.email},key=settings.JWT_SECRET,algorithm='HS256')
                    print(data)

                    EmailTokenTemplates.verify_email(user, data)

                    return Response({'message':'To Active Account Check Email '},status=HTTP_201_CREATED)
                else:
                    return Response({"message": "Password and Conform Password both are same", "code": 400},
                                    status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_400_BAD_REQUEST)
        

class EmailVerify(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):

            token = self.request.GET['token']
            otp_token = jwt.decode(token, settings.JWT_SECRET, algorithms='HS256')
            user = Profile.objects.get(email=otp_token['email'])

            if not user.email_verified:
                user.email_verified = True
                user.save()
                return Response({"message": "Email verified successfully, Please login", "code": 200},
                                status=HTTP_200_OK)
            else:
                return Response({"message": "Invalid otp token", "code": 400}, status=HTTP_400_BAD_REQUEST)

class LoginViewset(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            auth = RegisterAuthBackend()
            # user = Profile.objects.get(email= data['email'],password=data['password'])

            user = Profile.objects.get(email=data['email'])
            user.check_password(data['password'])
            if user:
                if user.is_admin:
                    if user.is_active:
                        if user.email_verified:
                            token = RefreshToken.for_user(user)
                            token = {
                                "access_token": str(token.access_token),
                                "refresh_token": str(token),
                                "is_admin": user.is_admin,
                                "message": "Login success",
                                "code": 200
                            }
                            return Response(token, status=HTTP_200_OK)
                        else:
                            return Response({'msg':'Email is Not Verified ','code':400},status=HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"msg":'your account not activated..!','status_code':400})
                else:
                    if user.is_active:
                        if user.email_verified:
                            token = RefreshToken.for_user(user)
                            token = {
                                "access_token": str(token.access_token),
                                "refresh_token": str(token),
                                "is_active": user.is_active,
                                "message": "Login success",
                                "code": 200
                            }
                            return Response(token, status=HTTP_200_OK)
                        else:
                            return Response({'msg':'Email is Not Verified..','code':400},status=HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"msg":'your account not activated..!','status_code':400})
            return Response({'msg':'invalid user','code':400},status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_400_BAD_REQUEST)

class LogOutViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def create(self,request,*args,**kwargs):
        try:
            data = request.data

            validate = validate_args(data,['refresh_token'])
            if validate:
                return validate

            try:
                refresh_token = data['refresh_token']
                token = RefreshToken(refresh_token)
                token.blacklist()
                response_data = {
                    'status_code': HTTP_200_OK,
                    'message': 'LogedOut....'
                }
                return Response(response_data, status=HTTP_200_OK)
            except Exception as e:
                response_data = {
                    'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                    'error': str(e),
                    'message': 'Something went wrong.'
                }
                return Response(response_data,status=HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)


class ForgotPasswordViewset(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            validate = validate_args(data,['email'])
            if validate:
                return validate

            if not validate_email_address(data['email']):
                return Response({'message':'invalid format email...','code':400},status=HTTP_400_BAD_REQUEST)

            obj = Profile.objects.get(email=data['email'])

            if obj:
                created_time = int(time.time())
                expired_time = created_time + 300
                obj.mobile_otp = send_via_mail(data['email'])
                obj.mobile_otp_expired = expired_time
                obj.save()
                return Response({'msg':'otp sent on email ','code':200},status=HTTP_200_OK)
            else:
                return Response({"msg":'Invalid email Id ','code':400},status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)


class verifyOtpView(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            validate = validate_args(data,['email','mobile_otp'])
            if validate:
                return validate
            if not validate_email_address(data['email']):
                return Response({"msg":'Invalid format email id ','code':400},status=HTTP_400_BAD_REQUEST)

            obj = Profile.objects.get(email = data['email'])
            if obj:
                curent_time = int(time.time())
                if obj.mobile_otp_expired >= curent_time:
                    if obj.mobile_otp == data['mobile_otp']:
                        return Response({'msg':'otp matched..','code':200},status=HTTP_200_OK)
                    else:
                        return Response({'msg':'Wrong  Otp','code':400},status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'msg':'otp time expired ','code':400},status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'msg':'Invalid User','code':400},status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)



class ResendOtp(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            validate = validate_args(data, ['email'])
            if validate:
                return validate

            if not validate_email_address(data['email']):
                return Response({'message': 'invalid format email...', 'code': 400}, status=HTTP_400_BAD_REQUEST)

            obj = Profile.objects.get(email=data['email'])

            if obj:
                created_time = int(time.time())
                expired_time = created_time + 300
                obj.mobile_otp = send_via_mail(data['email'])
                obj.mobile_otp_expired = expired_time
                obj.save()
                return Response({'msg': 'otp sent on email ', 'code': 200}, status=HTTP_200_OK)
            else:
                return Response({"msg": 'Invalid email Id ', 'code': 400}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteProfile(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            validate = validate_args(data,['email','password'])
            if validate:
                return validate

            if not validate_email_address(data['email']):
                return Response({'msg':'Invalid format email id ','code':400},status=HTTP_400_BAD_REQUEST)

            obj = Profile.objects.get(email=data['email'])
            if obj:
                obj.delete()
                return Response({'msg':'Profile deleted ....','code':200},status=HTTP_200_OK)
            else:
                return Response({'msg':'User not found','code':400},status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            response_data = {
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)




class NewPasswordView(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            validate = validate_args(data,['email','password','password2'])
            if validate:
                return validate
            if not validate_email_address(data['email']):
                return Response({'msg':'invalid format email..','code':400},status=HTTP_400_BAD_REQUEST)

            if data['password'] and data['password'] != data['password2']:
                return Response({"msg":'Password and confirm password must be same ','code':400},status=HTTP_400_BAD_REQUEST)

            try:
                obj = Profile.objects.get(email__exact=data['email'])
                if obj:
                    obj.set_password(data['password'])
                    obj.save()
                    return Response({'msg': 'Password has been changed succesfully..', 'code': 200})
                else:
                    return Response({'msg': 'User not found', 'code': 400}, status=HTTP_400_BAD_REQUEST)

            except Exception as e:
                response_data = {
                    'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                    'error': str(e),
                    'message': 'Something went wrong.'
                }
                return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)


        except Exception as e:
            response_data = {
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)






















