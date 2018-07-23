from django.test import TestCase
from onlineapp.serializers import *
# Create your tests here.

class CollegeTestCase(TestCase):
    def setUp(self):
        self.college=College.objects.create(name='SV Engineering College',location='Tirupati',acronym='svce',contact='contact@svc.in')
        self.serializer=CollegeSerializer(self.college)

    def test_college_valid_serializer(self):
        self.assertEqual(self.serializer.data,{'name': 'SV Engineering College', 'location': 'Tirupati', 'acronym': 'svce', 'contact': 'contact@svc.in'})

