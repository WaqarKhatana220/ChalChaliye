from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('SignIn',views.SignIn,name="SignIn"),
    path('',views.HomePage,name="HomePage"),
    path('SignUp',views.SignUp,name="SignUp"),
    path('Help',views.Help,name="Help"),
    path('SignOut',views.SignOut,name="SignOut"),
    path('Contact',views.Contact,name="Contact"),
]