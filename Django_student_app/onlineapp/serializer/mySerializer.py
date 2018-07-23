from rest_framework import serializers ,routers, viewsets

from onlineapp.models import *




# class CollegeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = College
#         fields = ('id', 'name', 'location', 'acronym', 'contact')


class CollegeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    # exclude={'id'}
    name = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=64)
    acronym = serializers.CharField(max_length=8)
    contact = serializers.EmailField()

    def create(self, validated_data):
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance



class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model=MockTest1
        fields = ('problem1','problem2','problem3','problem4','total')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # exclude = ['college']
        fields = '__all__'







class StudentDetailsSerializer(serializers.ModelSerializer):
    mocktest=MockTestSerializer()
    class Meta:
        model=Student
        fields='__all__'

    def create(self, validated_data):
        marks_data=validated_data.pop('mocktest')
        student=Student.objects.create(**validated_data)
        student.mocktest=MockTest1.objects.create(student=student,**marks_data)
        return student


    def update(self, instance, validated_data):
        mockdata = validated_data.pop('mocktest')

        instance.name = validated_data['name']
        instance.dropped_out=validated_data['dropped_out']
        instance.db_folder=validated_data['db_folder']
        instance.email=validated_data['email']
        instance.college=validated_data['college']


        mocktest = instance.mocktest
        instance.mocktest.problem1=mockdata['problem1']
        instance.mocktest.problem2 = mockdata['problem2']
        instance.mocktest.problem3 = mockdata['problem3']
        instance.mocktest.problem4 = mockdata['problem4']
        instance.mocktest.total=mockdata['total']
        instance.mocktest.save()
        instance.save()


        instance.marks=mocktest
        return instance





















# class StudentDetailsSerializer(serializers.ModelSerializer):
#     mocktest=MockTestSerializer()
#     class Meta:
#         model=Student
#         fields=('name','dob','email','dropped_out','college','db_folder','mocktest')
#         # fields='__all__'
#
#     def create(self,validated_data):
#         # user_data = validated_data.pop('student_id')
#         # print(user_data)
#         # mocktest = MockTestSerializer.create(MockTestSerializer(), validated_data=user_data)
#         # student, created = Student.objects.update_or_create(mocktest=mocktest)
#
#
#         mocktest=validated_data.pop('mocktest')
#         student=Student.objects.create(**validated_data)
#         mocktestmarks=MockTest1.objects.create(student=student,**mocktest)
#         return student
#
#     def update(self, instance, validated_data):
#         user_data = validated_data.pop('student_id')
#         mocktest = MockTestSerializer.update(MockTestSerializer(), validated_data=user_data)
#         student, created = Student.objects.update(mocktest=mocktest)
#         return student
#



# class StudentDetailSerializer(serializers.Serializer):
#     student= StudentSerializer()
#
#     class Meta:
#         model = MockTest1
#         fields = ('problem1', 'problem2', 'problem3', 'problem4', 'total', 'student')
#

    # name = models.CharField(max_length=128)
    # dob = models.DateField(null=True, blank=True)
    # email = models.EmailField()
    # db_folder = models.CharField(max_length=50)
    # dropped_out = models.BooleanField(default=False)
    # college = CollegeSerializer()
    # problem1 = models.IntegerField()
    # problem2 = models.IntegerField()
    # problem3 = models.IntegerField()
    # problem4 = models.IntegerField()
    # total = models.IntegerField()
    # student = StudentSerializer()



# college=CollegeSerializer(required=True)
    # name = serializers.CharField(max_length=128)
    # dob = serializers.DateField()
    # email = serializers.EmailField()
    # db_folder = serializers.CharField(max_length=50)
    # dropped_out = serializers.BooleanField(default=False)
    #



    # college = serializers.RelatedField(source='college', read_only=True)

    # class Meta:
    #     model = Student
    #     fields = ('name', 'dob', 'email','db_folder','dropped_out')