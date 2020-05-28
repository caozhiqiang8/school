from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.views.generic import View
# Create your views here.
#登录
class Login(View):

    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        if user == 'admin' and pwd == '1111':
            return redirect('/school/')
        else:
            msg = '用户名密码错误'
            return render(request, 'login.html', {'masg': msg})
