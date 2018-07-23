import django,os,sys
os.environ['DJANGO_SETTINGS_MODULE']="onlineproject.settings"
django.setup()
from onlineapp.models import *
import psutil

manager=College.objects
querySets=College.objects.all()


#
all=psutil.pids()
print(all)
import os
# a=os.getpid()
# all=psutil.users()
# print(all)
# p = psutil.Process()

for i in all:
    process = psutil.Process(i)
    a=process.memory_info()[0]
    b=process.name()
    c=i
    print(a,b,c)
    # print(list(a))
    # a.data
    # print(a.data)
    # mem = process.memory_percent()
    # print(a)



#
# import os
# pids = []
# a = os.popen("tasklist").readlines()
# for x in a[3:]:
#     pids.append((x[:28],int(x[29:34]),int((x[64:74].strip().replace(",","")))))
#
#
# # for each in pids:
# #     print(each)
#
#
# info=[]
# for each in pids:
#     info.append({'name':each[0],'pid':each[1],'memory_usage':each[2]})
# a=sorted(info,key =lambda v : v['memory_usage'])
# print(a)
#
