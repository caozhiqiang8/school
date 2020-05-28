from django.urls import path
from django.conf.urls import url
from school.views import SchoolIndex


urlpatterns = [
    path('',SchoolIndex.as_view(),name = 'school')

]