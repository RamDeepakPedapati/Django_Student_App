import django,os,sys
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from django.forms import forms
from django.forms import ModelForm
from django import forms
os.environ['DJANGO_SETTINGS_MODULE']="onlineproject.settings"
django.setup()
from onlineapp.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, loader, get_object_or_404
from django.shortcuts import render_to_response
from django.views import View
from django.views.generic import ListView, DetailView ,CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from django.contrib import messages



class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name '})
    )
    last_name = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name '})
    )

    username = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Nsme'})
    )

    password = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'First Name '})
    )





class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,template_name='SignUpForm.html',context={'form':form,'title':'Signup | Online App'})

    def post(self,request):
        form =SignUpForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            # import ipdb
            # ipdb.set_trace()

            user=authenticate(
            request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('onlineapp:collegeshtml')
            else:
                messages.error(request,'Invalid Credentials')
        # return render(redirect,template_name='SignUpForm.html',context={'form':form,'title':'Signup | Online App'})





class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Nsme'})
    )

    password = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'First Name '})
    )




class LoginView(View):

    def get(self,request):
        form = LoginForm()
        return render(request,template_name='LoginForm.html',context={'form':form,'title':'Signup | Online App'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('onlineapp:collegeshtml')
            else:
                messages.error(request, 'Invalid Credentials')

        return render(request,template_name='collegeshtml')





def logout_user(request):
    logout(request)
    return redirect('onlineapp:login')
