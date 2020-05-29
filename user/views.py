from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):
    message_flag = 0
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username) and User.objects.filter(email=email) and User.objects.filter(password=password):
            message_flag = -1
            return render(request, 'user/register.html', {'message_flag': message_flag})
        else:
            u = User(username=username, email=email, password=password)
            u.save()
            message_flag = 1
            return render(request, 'user/register.html', {'message_flag': message_flag})
    return render(request, 'user/register.html', {'message_flag': message_flag})    

def login(request):
    message_flag = 0
    if request.method == 'POST':
        username = request.POST['email'] 
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return redirect("voting_app/host_event_page.html")
        else:
            message_flag = 1    
    return render(request, "user/login.html", {'message_flag': message_flag})