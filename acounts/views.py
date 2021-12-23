from django.shortcuts import render
from .forms import UserForm,ProfileForm,UserEditForm,ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()
            profile = profileform.save(commit=False)
            profile.user=user
            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']
            profile.save()
        else:
            print(userform.errors,profileform.errors)
        group = Group.objects.get(name = 'customers')
        user.groups.add(group)
        return HttpResponseRedirect(reverse('accounts:login'))
    else:
        userform = UserForm()
        profileform = ProfileForm()
    
    

    return render(request,'registration/register.html',{
        'userform':userform,'profileform':profileform
    })   
    
def log_in(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('products:home'))
        else:
            return HttpResponse('invalid user')
    else:
        return render(request,'registration/loginn.html')

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('products:home'))


@login_required
def	edit(request):
    if request.method == 'POST':								
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('products:dashboard'))
    else:
        user_form =	UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return	render(request,'registration/edit.html',{'user_form': user_form,'profile_form': profile_form})
@login_required
def profile(request):
    return render(request, 'registration/prof.html')