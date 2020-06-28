from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,HttpResponseRedirect
from django.views.generic import View


class resource(View):

    def get(self,request):
        return render(request,'resource.html')
    
    def post(self,request):
        return render(request,'resource.html')
