from django.urls import path
from django.conf.urls import url
from login import views
from login.views import Login,Login_test


urlpatterns = [
    path('',Login.as_view(),name = 'login'),
    path('test/',Login_test.as_view(),name = 'login_test')


]