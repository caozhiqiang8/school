from django.views.generic import View
from django.shortcuts  import render,redirect,HttpResponse

class SchoolIndex(View):
    def get(self,request):
        return render(request,'404.html')

    def post(self,request):
        return render(request,'404.html')
