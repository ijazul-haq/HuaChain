from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Artwork


def index(request):
    return render(request, 'website/index.html')


def gallery(request):
    return render(request, 'website/index.html')


@login_required
def collection(request):
    public_key = request.user.userprofile.public_key
    collection = Artwork.objects.filter(artist=public_key)

    data = {
        'collection': collection,
    }
    return render(request, 'user/collection.html', data)


@login_required
def log_out(request):
    logout(request)
    return redirect('index')


def user_login(request):
    if request.method == 'POST':
        data = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('collection')
            else:
                data['form_errors'] = 'User is not active'
        else:
            data['form_errors'] = 'User not found'
        return render(request, 'user/login.html', data)
    else:
        return render(request, 'user/login.html')


def user_reg(request):
    user_form = UserForm
    profile_form = ProfileForm

    data = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        data['user_form'] = user_form
        data['profile_form'] = profile_form

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # keys = generate_keypair()
            # profile.public_key = keys.public_key
            # profile.private_key = keys.private_key
            profile.save()

            return redirect('user_login')
        else:
            data['form_errors'] = 'Invalid Form'
            return render(request, 'user/register.html', data)
    else:
        return render(request, 'user/register.html', data)
