import django,os,sys
os.environ['DJANGO_SETTINGS_MODULE']="onlineproject.settings"
django.setup()
from onlineapp.models import *


# Create your views here


from django.http import HttpResponse
from django.shortcuts import render, redirect ,loader
from django.shortcuts import render_to_response
from django.views import View


def some_view(request):
   f=open("tic_tac_toe.html","r")
   return HttpResponse(f)
   # return redirect('http://example.com/')
   # return redirect('tic_tac_toe.html')


def tic_tac_toe(request):
    template = loader.get_template("tic_tac_toe.html")
    return HttpResponse(template.render())


def hello(request):
    return HttpResponse('<h1>Hello, World!<h1>')


def welcome(request):
    return HttpResponse('welcome')



def college_details(request):
    c=list(College.objects.values('name','acronym'))
    html_string=''
    html_string=html_string+'<html><table style="border:5;"><tr><th>College</th><th>Acronym</th></tr>'
    for i in c:
        html_string=html_string+"<tr><td>"+i['name']+"</td>"
        html_string=html_string+"<td>"+i['acronym']+"</td></tr>"
    html_string=html_string+"</table></html>"
    return HttpResponse(html_string)


def colleges(request):
    c=list(College.objects.values('name','acronym'))
    html_string = ''
    html_string = html_string + '<html><table style="border:5;"><tr><th>College</th><th>Acronym</th></tr>'
    for i in c:
        html_string = html_string + "<tr><td>" + i['name'] + "</td>"
        html_string = html_string + "<td>" + i['acronym'] + "</td></tr>"
    html_string = html_string + "</table></html>"
    resp=HttpResponse()
    resp.write(html_string)
    return resp



def clg_index(request):


    # c_object = College.objects.values('name','acronym')
    # template = loader.get_template('onlineapp/colleges.html')
    # context = {
    #     'c_object': c_object,
    # }
    # return HttpResponse(template.render(context, request))

    c_object = College.objects.values('name','acronym')
    context = {'c_object': c_object}
    return render(request, 'colleges.html', context)



def student_details(request):
    c_object = Student.objects.values('name','email','college__acronym')
    context = {'c_object': c_object}
    return render(request, 'studentdetails.html', context)





#this function is used for requesting using like   /?q=<somevalue> at the end
# def student_detail(request):
#     id=request.GET.get('q',' ')
#     c_object = Student.objects.values('name','email','college__acronym').filter(id=id)
#     context = {'c_object': c_object}
#     return render(request, 'studentdetails.html', context)



def student_detail(request,value):
    c_object = Student.objects.values('name','email','college__acronym').filter(id=value)
    #   c_object = Student.objects.values('name', 'email', 'college__acronym').get(id=value)
    context = {'c_object': c_object}
    return render(request,'studentdetails.html', context)

def student_total(request):
    c_object = Student.objects.values('id','name','email','mocktest1__total','college__acronym')
    #   c_object = Student.objects.values('name', 'email', 'mocktest1__acronym').get(id=value)
    context = {'c_object': c_object}
    return render(request,'student_total.html', context)

def college_stats(request,clg):
    c_object=College.objects.values('student__name','student__mocktest1__total','name').filter(acronym=clg).order_by('-student__mocktest1__total')
    context={'c_object':c_object}
    return render(request,'clg_stats.html',context)




def students(request):
    s_object=Student.objects.values('id','name','email','db_folder','college__acronym').order_by('id')
    context = {'s_object': s_object}
    return render(request, 'students.html', context)


def Profile(request,id):
    s_object=Student.objects.values('id','name','email','db_folder','college__name','mocktest1__problem1','mocktest1__problem2','mocktest1__problem3','mocktest1__problem4','mocktest1__total').filter(id=id)
    context = {'s_object': s_object}
    return render(request, 'profile.html', context)





def test_session(request):
    request.session.setdefault("counter",0)
    call_count=request.session["counter"]+1
    request.session["counter"]=call_count

    return HttpResponse("The session call count is"+str(call_count))



def test(request):
    return HttpResponse("testing...........")

def raise_error(request):
    raise ValueError













# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         return 'Hello, World!'
#         # return HttpResponse('Hello, World!')c=C