from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from onlineapp.models import College
from onlineapp.serializer import CollegeSerializer

import base64
from django.contrib.auth import authenticate
from django.http import JsonResponse


def basic_authentication(data_function):
    def wrapper(request,*args,**kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    username, password = base64.b64decode(auth[1]).split(b':', 1)
                    username=username.decode('utf-8')
                    password=password.decode('utf-8')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        return data_function(request)

            # otherwise ask for authentification
        return JsonResponse({'WWW-Authenticate':'Basic realm="restricted area"'},status=401)
    return wrapper




# @basic_authentication
@csrf_exempt
def college_list(request):
    if request.method == 'GET':
        snippets = College.objects.all()
        serializer = CollegeSerializer(snippets, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        # print(request.data)
        serializer = CollegeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



# @basic_authentication
@csrf_exempt
def college_detail(request, pk):
    try:
        snippet = College.objects.get(id=pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollegeSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CollegeSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



