from django.urls import path
from blog.views import *
from blog.register import  *
app_name='blog'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/',RegisterView.as_view())
]