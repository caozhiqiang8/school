from django.views.generic import View
from django.shortcuts  import render,redirect,HttpResponse

class schoolIndex(View):
    def get(self,request):
        return render(request,'school.html')

    def post(self,request):


        
        return render(request,'school.html')
