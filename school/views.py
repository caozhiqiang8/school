from django.views.generic import View
from django.shortcuts  import render,redirect,HttpResponse

class SchoolIndex(View):
    def get(self,request):
        return render(request,'school_index.html')

    def post(self,request):
        return render(request,'school_index.html')
