from django.urls import path
from django.conf.urls import url
from user.views import userIndex


urlpatterns = [
    path('',userIndex.as_view(),name = 'user')

]