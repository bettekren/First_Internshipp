from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
def register(request):
  form = RegisterForm(request.POST or None) #Django sağlıyor Post mu Get mi olduğunu kontrol etmek zorunda kalmıyorum.
  if form.is_valid():
      username = form.cleaned_data.get("username")
      print("username:", username)
      password = form.cleaned_data.get("password")
      newUser = User(username  = username)
      newUser.set_password(password)
      newUser.save()
      login(request, newUser)#Kayıt olduktan sonra otomatikolarak sisteme giriş yapıyor
      messages.info(request, "Profile details updated.")
      return redirect("index")
  context = {
        "form" : form  #sözlük yapısı
      }  
  return render(request, "register.html",context)  
  
def loginUser(request):
   form = LoginForm(request.POST or None)
   context = {
      "form" : form
   }
   if form.is_valid():
      username = form.cleaned_data.get("username")
      print("username:", username)
      password = form.cleaned_data.get("password")
      user = authenticate(username = username, password = password)
      if user is None:
         messages.info(request,"Username or password is wrong")
         return render(request,"login.html", context)
      messages.success(request, "Login is succesful")
      login(request,user)
      return redirect("index")
   return render(request, "login.html", context)

def logout(request):
   messages.success(request, "Logout is successful")
   return redirect("index")


