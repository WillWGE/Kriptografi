from django.urls import path
from . import views

urlpatterns=[
    path('',views.vigenere,name='vigenere'),
    #extcipher
    path('extcipher',views.extcipher,name='extcipher'),
    #playfaircipher
    path('playfair',views.playfair,name='playfair'),
    #otpcipher
    path('onetimepad',views.otpcipher,name='onetimepad')

] 