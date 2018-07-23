import django,os,sys
from django.contrib.auth import logout
from django.forms import forms
from django.forms import ModelForm
from django import forms
from rest_framework.decorators import api_view
from rest_framework.response import Response

os.environ['DJANGO_SETTINGS_MODULE']="onlineproject.settings"
django.setup()
from onlineapp.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, loader, get_object_or_404
from django.shortcuts import render_to_response
from django.views import View
from django.views.generic import ListView, DetailView ,CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AddCollege(ModelForm):
    class Meta:
        model=College
        exclude={'id'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name of the college'}),
            'acronym':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter acronym of the college'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location of the college'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact of the college'})
        }




class CreateCollegeView(LoginRequiredMixin,CreateView):
    model = College
    login_url = '/login/'
    form_class = AddCollege
    template_name = 'collegeForm.html'
    success_url = reverse_lazy('onlineapp:collegeshtml')





class UpdateCollegeView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = College
    login_url = '/login/'
    permission_required = "onlineapp.change_college"
    permission_denied_message = "user does not have permission to change a college info"
    raise_exception = True
    form_class = AddCollege
    template_name = 'collegeForm.html'
    success_url = reverse_lazy('onlineapp:collegeshtml')



class DeleteCollegeView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model=College
    login_url = '/login/'
    permission_required = "onlineapp.delete_college"
    permission_denied_message = "user doest not have permission to delete a college"
    raise_exception = True
    template_name = 'ConfirmDeleteCollege.html'
    success_url = reverse_lazy('onlineapp:collegeshtml')





# class CollegeView(View):
#
#     def get(self,request,*args,**kwargs):
#         form=AddCollege()
#         if kwargs:
#             college=College.objects.get(**kwargs)
#             form=AddCollege(instance=college)









class CollegeDetailView(LoginRequiredMixin,DetailView):
    template_name = 'clg_stats.html'
    login_url = '/login/'
    model=College

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context=super(CollegeDetailView,self).get_context_data(**kwargs)
        college=context.get('college')
        context['college_name']=college.name
        context['collegeID'] = college.id

        students=list(College.objects.values('id','student__id','student__name','student__mocktest1__total','name').filter(acronym=college).order_by('-student__mocktest1__total'))
        context.update({
            'students':students,
            'user_permissions':self.request.user.get_all_permissions()
        })



        return context




class CollegeListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = College
    context_object_name = 'colleges'
    template_name = 'college.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context=super(CollegeListView,self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions, 'title': 'College Details', })
        return context



class CollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        colleges=College.objects.all()
        return render(request,template_name='college.html',context={
            'colleges':colleges
        })









