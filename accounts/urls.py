from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *



accounts = DefaultRouter()

accounts.register('profile',Profile_Register,basename='profile')
accounts.register('Login',LoginViewset,basename='Login')
accounts.register('LogOut',LogOutViewset,basename='LogOut')
accounts.register('ForgotPassword',ForgotPasswordViewset,basename='ForgotPassword')
accounts.register('verifyOtpView',verifyOtpView,basename='verifyOtpView')
accounts.register('ResendOtp',ResendOtp,basename='ResendOtp')
accounts.register('DeleteProfile',DeleteProfile,basename='DeleteProfile')
accounts.register('NewPassword',NewPasswordView,basename='NewPassword')
accounts.register('Verify_Email',EmailVerify,basename='Verify_Email')
accounts.register('Delete_EmailUser',DeleteEmailUser,basename='Delete_EmailUser')

urlpatterns = [
    path('',include(accounts.urls)),
]