from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import View, CreateView, FormView
from django.urls import reverse_lazy
from .forms import SignUpForm, ContactLawyer
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

#registration view function
class RegisterView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request,'accounts/signup.html')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            return redirect('signin')
        return render(request,'accounts/signup.html', {'form':form})

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

@login_required #users can't have access to this view unless they log in
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile_page.html')


class ContactLawyerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/lawyer.html')

    def post(self,request, *args, **kwargs):
        form = ContactLawyer(request.POST)
        message = request.POST['message']
        if form.is_valid():
            send_mail('Contact Lawyer', message, settings.EMAIL_HOST_USER, ['kadelcode@gmail.com'], fail_silently=False)
            messages.info(request,"Message successfully sent")
            return redirect('contact_dashboard')
        return render(request, 'accounts/lawyer.html', {'form':form})

'''def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Need a Lawyer', message, settings.EMAIL_HOST_USER, ['kadelcode@gmail.com'], fail_silently=False)
        messages.info(request,"Message successfully sent.")
        return redirect('contact_dashboard')
    else:
        return render(request, 'accounts/lawyer.html')'''

@login_required
def history(request):
    return render(request, 'accounts/history.html')