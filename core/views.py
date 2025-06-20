from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Category,Course,Lesson,Material,Enrollment,QuestionAnswer
from .serializers import CategorySerializers,CourseSerializers,LessonSerializers,MaterialSerializers,EnrollmentSerializers,QuestionAnswerSerializers
# Create your views here.

@api_view(['GET','POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        if request.user.role != 'admin':
            return Response({"detail":"only admin can create categories"},status=403)
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['GET','POST'])
def course_list_create(request):
    if request.method == 'GET':
        if request.user.role  in ['admin','student']:
            courses = Course.objects.all()
        elif request.user.role == 'teacher':
            courses = Course.objects.filter(teacher=request.user)
        else:
            return Response({"detail":"you are not authorized to view this page"}, status=403)

        serializer = CourseSerializers(courses, many=True)
        return Response(serializer.data)


    elif request.method=='POST':
        if request.user.role != 'teacher':
            return Response({"detail":"only teacher can create Course"},status=403)
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)