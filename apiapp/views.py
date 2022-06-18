from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import PersonalDetailsSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import Http404

# App views
def home(request):
    persons = PersonalDetails.objects.all()
    
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Age= request.POST['age']
        gender= request.POST['gender']
        speciality = request.POST['speciality']
        campus = request.POST['campus']
        
        new_person = PersonalDetails.objects.create(first_name=first_name, last_name=last_name, Age=Age, gender=gender, speciality=speciality, campus=campus)
        
        new_person.save()
        return redirect('home')
    return render(request, 'index.html', {'persons':persons})


def next(request):
    return render(request, 'next.html')


class PersonalDetailsList(APIView):
    def get(self, request, format=None):
        #querying from the database(students table)
        students = PersonalDetails.objects.all()
        serializers = PersonalDetailsSerializer(students, many=True)
        
        #JSON RESPONSE
        return Response(serializers.data)
        
    permission_classes = (IsAdminOrReadOnly,)
    
    def post(self, request, format=None):
        serializers = PersonalDetailsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
    
#accessing a single item
class PersonalDetailsDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_single_student(self, pk):
        try:
            return PersonalDetails.objects.get(pk=pk)
        except PersonalDetails.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        single_student = self.get_single_student(pk)
        serializers = PersonalDetailsSerializer(single_student)
        return Response(serializers.data)
    
    #PUT ---> Update our single item    
    def put(self, request, pk, format=None):
        single_student = self.get_single_student(pk)
        serializers = PersonalDetailsSerializer(single_student, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    #    DELETE METHOD
    def delete(self, request, pk, format=None):
        delete_student = self.get_single_student(pk)
        delete_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
