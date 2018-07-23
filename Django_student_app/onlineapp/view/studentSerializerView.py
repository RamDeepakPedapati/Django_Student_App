from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json

from onlineapp.models import Student, MockTest1
from onlineapp.serializer import StudentSerializer
from onlineapp.serializer import MockTestSerializer
from onlineapp.serializer import StudentDetailsSerializer
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentListApi(APIView):

    def get(self, request, *args,**kwargs):
        snippets = Student.objects.values().filter(college_id=self.kwargs.get('pk'))
        serializer = StudentSerializer(snippets, many=True)
        return JsonResponse(serializer.data)

    def post(self, request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class AllStudentListApi(APIView):
    def get(self, request, *args,**kwargs):

        snippets = Student.objects.all().filter(college_id=kwargs.get('pk'))
        serializer = StudentSerializer(snippets, many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self, request,*args,**kwargs):
        data=request.data
        data['college']=kwargs.get('pk')
        serializer = StudentDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentDetailApi(APIView):

    def get(self, request, *args,**kwargs):
        snippets =Student.objects.get(pk=kwargs.get('student_id'))
        mocktest=MockTest1.objects.get(student_id=kwargs.get('student_id'))
        snippets.mocktest =mocktest

        serializer = StudentDetailsSerializer(snippets)
        return JsonResponse(serializer.data)

    def put(self,request,*args,**kwargs):
        student= Student.objects.get(id=kwargs.get('student_id'))
        # student.mocktest = MockTest1.objects.filter(student_id=kwargs.get('student_id'))

        student.mocktest=MockTest1.objects.filter(student_id=kwargs.get('student_id'))[0]

        serializer = StudentDetailsSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def delete(self, request,pk,student_id,format=None):
        student = Student.objects.get(id=student_id)
        student.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
