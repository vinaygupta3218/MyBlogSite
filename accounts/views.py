from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        if User.objects.filter(username = request.POST['emailid']).exists():
            messages.error(request, "User is already registered")
            return render(request, 'register.html')
        else:
            user = User()
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['emailid']
            user.username = request.POST['emailid']
            user.password = make_password(request.POST['password'])
            user.save()
            profile = Profile()
            profile.user = user
            profile.save()
            messages.success(request,
            "You have registered successfully")
            return redirect('login')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['emailid'],
            password = request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect('viewallarticles')
        else:
            messages.error(request,
            "Invalid username/password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'viewprofile.html',
    {'user': request.user})

@login_required(login_url='login')
def edit_profile_view(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['emailid']
        user.username = request.POST['emailid']
        user.save()
        profile = Profile.objects.get(
        user_id = request.user.id)
        profile.photo = request.FILES['photo']
        profile.save()
        messages.success(request,
        "Profile details are updated successfully")
        return redirect('viewprofile')
    else:
        return render(request, 'editprofile.html',
        {'user': request.user})

@login_required(login_url='login')
def change_password_view(request):
    if request.method == 'POST':
        if check_password(request.POST['oldpassword'], request.user.password):
            if request.POST['newpassword'] == request.POST['confirmpassword']:
                user = User.objects.get(id = request.user.id)
                user.password = make_password(request.POST['newpassword'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password is changed successfully")
                return render(request, 'ChangePassword.html')
            else:
                messages.error(request, "New password and confirmed password didn't match")
                return render(request, 'ChangePassword.html')
        else:
            messages.error(request, "Old password is incorrect")
            return render(request, 'ChangePassword.html')
    else:
        return render(request, 'ChangePassword.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')
