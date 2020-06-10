from django.urls import path
from django.conf.urls import url
from user.views import userIndex,userTea,userStu


urlpatterns = [
    path('',userIndex.as_view(),name = 'user'),
    path('teacher/',userTea.as_view(),name = 'teacher'),
    path('student/',userStu.as_view(),name = 'student'),

]