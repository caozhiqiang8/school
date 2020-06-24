import json

from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,HttpResponseRedirect
from django.views.generic import View
# Create your views here.
#登录


class Login(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        user = request.POST.get('user_name', None)
        pwd = request.POST.get('pass_word', None)
        if user == 'admin' and pwd == '1111':
           data = {
               'status':0,
               'url':'/user/'
           }
           return  HttpResponse(json.dumps(data))
        else:
            data = {
                'status': 1,
                'url': '/login/'
            }
            return HttpResponse(json.dumps(data))
