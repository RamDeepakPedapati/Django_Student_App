import django,os

os.environ['DJANGO_SETTINGS_MODULE']="onlineproject.settings"
django.setup()

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from onlineapp.models import *



class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, College):
            return str(obj)
        return super().default(obj)


data=serialize('json',College.objects.all(),cls=LazyEncoder)
print(data)


