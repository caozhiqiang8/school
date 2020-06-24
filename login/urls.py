from django.urls import path
from django.conf.urls import url
from login import views
from login.views import Login


urlpatterns = [
    path('',Login.as_view(),name = 'login'),


]