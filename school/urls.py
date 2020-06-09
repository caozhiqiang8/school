from django.urls import path
from django.conf.urls import url
from school.views import schoolIndex


urlpatterns = [
    path('',schoolIndex.as_view(),name = 'school')

]