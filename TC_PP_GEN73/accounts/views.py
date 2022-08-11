from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import View, CreateView, FormView
from django.urls import reverse_lazy
from .forms import SignUpForm


# Create your views here.

#registration view function
class RegisterView(FormView):
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            return redirect('signin')
        return render(request,'accounts/signup.html', {'form':form})

    def get(self, request, *args, **kwargs):
        return render(request,'accounts/signup.html')

<<<<<<< HEAD
=======
#login function
def login_view(request):
    if request.method == 'POST':
        #username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email = email, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        
        else:
            messages.info(request, 'Invalid Credentials. Please Login with the right details.')
            return redirect('signin')
    return render(request, 'accounts/signin.html')



def logout(request):
    auth.logout(request)
    return redirect('home')

>>>>>>> 326ef46ad1a14825d99275235f6e6ed44dbea94c
@login_required #users can't have access to this view unless they log in
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile_page.html')

def contact(request):
    return render(request, 'accounts/lawyer.html')

def history(request):
    return render(request, 'accounts/history.html')