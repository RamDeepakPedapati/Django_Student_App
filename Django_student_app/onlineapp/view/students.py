import django,os,sys
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
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AddStudent(ModelForm):
    class Meta:
        model=Student
        exclude={'id','dob','college'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name of the student'}),
            'email':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email of the Email'}),
            'db_folder':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter DB Folder Name'}),
            'dropped_out':forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter Dropped out of the Is Dropped'})

        }



class AddMockTest1(ModelForm):
    class Meta:
        model=MockTest1
        exclude={'student','total'}
        widgets={
            'problem1':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter marks of problem1'}),
            'problem2':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter marks of problem2'}),
            'problem3':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter marks of problem3'}),
            'problem4':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter marks of problem4'}),
        }





class CreateStudentView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Student
    form_class = AddStudent
    template_name = 'studentForm.html'

    def get_context_data(self, **kwargs):
        context=super(CreateStudentView,self).get_context_data(**kwargs)
        test_form=AddMockTest1()
        context.update({'student_form':context.get('form'),'test_form':test_form})
        return context


    def post(self,request,*args,**kwargs):

        college = get_object_or_404(College,pk=kwargs['college_id'])
        student_form = AddStudent(request.POST)
        test_form = AddMockTest1(request.POST)


        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()
            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()
        return redirect('onlineapp:collegesmarks', self.kwargs.get('college_id'))


class UpdateStudentView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Student
    form_class = AddStudent
    template_name = 'studentForm.html'
    permission_required = "onlineapp.change_student"
    permission_denied_message = "user does not have permission to change a student info"
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')

        test_form = AddMockTest1(instance=student_form.mocktest1)
        # import ipdb
        # ipdb.set_trace()

        context.update({'student_form': context.get('form'),'test_form': test_form})
        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = AddStudent(request.POST, instance=student)
        test_form = AddMockTest1(request.POST, instance=student.mocktest1)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())
        form.save()
        test_form.save()
        return redirect("onlineapp:collegesmarks", self.kwargs.get('college_id'))



class DeleteStudentView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = '/login/'
    model=Student
    template_name = 'ConfirmDeleteCollege.html'
    success_url = reverse_lazy('onlineapp:collegeshtml')
    permission_required = "onlineapp.delete_student"
    permission_denied_message = "user does not have permission to delete a student info"
    raise_exception = True

    def get(self,request,*args,**kwargs):
         return self.post(request,args,kwargs)

    def post(self,request,*args,**kwargs):
        self.delete(request,args,kwargs)
        return redirect("onlineapp:collegesmarks", self.kwargs.get('college_id'))





        # success_url = reverse_lazy('onlineapp:collegesmarks', self.kwargs.get('college_id'))


    # def get(self,request,*args,**kwargs):
    #     # import ipdb
    #     # ipdb.set_trace()
    #
    #
    #     college_id=self.kwargs.get('college_id')
    #     return self.post(request,args,kwargs)




# from onlineapp.serializers import StudentSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Student.objects.all()
#         serializer = StudentSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#






