from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.  

class Index(LoginRequiredMixin, View):
  # login_url: "/login/"
  # redirect_field_name: '/'
  template_name = "index.html"  
  def get(self, request):
    return render(request, "index.html")

class Login(View):
  def get(self, request):
    return render(request, "login.html")

  def post(self, request):
    username = request.POST['username']
    password =  request.POST['password']
    user = authenticate(request, username= username, password= password)

    if user is not None:
      login(request, user)
      return redirect('/')


