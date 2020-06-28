from django.urls import path
from django.conf.urls import url
from resource.views import resource

urlpatterns = [
    path('',resource.as_view(),name = 'resource'),

]