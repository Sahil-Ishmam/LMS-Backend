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
            courses = Course.objects.filter(instructor_id=request.user)
        else:
            return Response({"detail":"you are not authorized to view this page"}, status=403)

        serializer = CourseSerializers(courses, many=True)
        return Response(serializer.data)


    elif request.method=='POST':
        if request.user.role != 'teacher':
            return Response({"detail":"only teacher can create Course"},status=403)
        serializer = CourseSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(instructor_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'detail':'please login'})



@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request,pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({'detail':'Course Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if request.user.role =='admin' or request.user.role == course.instructor_id:
            serializer = CourseSerializers(course)
            return Response(serializer.data)
        return Response({'detail':'Permission Denied'},status=403)
    elif request.method == 'PUT':
        if request.user.role != 'teacher' or request.user != course.instructor_id:
            return Response({'detail':'only course teacher can update the course'}, status=403)
        serializer = CategorySerializers(Course,data=request.data)
        if serializer.is_valid():
            serializer.save(instructor_id = request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if request.user.role != 'teacher' or request.user != course.instructor_id:
            return Response({'detail':'only course teacher can delete the course'}, status=403)
        course.delete()
        return Response({'detail':'course deleted'},status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET','POST'])
def lesson_list_create(request):
    if request.method == 'GET':
        categories = Lesson.objects.all()
        serializer = LessonSerializers(categories, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = LessonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['GET','POST'])
def material_list_create(request):
    if request.method == 'GET':
        categories = Material.objects.all()
        serializer = MaterialSerializers(categories, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = MaterialSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['GET','POST'])
def enrollment_list_create(request):
    if request.method == 'GET':
        categories = Enrollment.objects.all()
        serializer = EnrollmentSerializers(categories, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = EnrollmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST'])
def questionanswer_list_create(request):
    if request.method == 'GET':
        categories = QuestionAnswer.objects.all()
        serializer = QuestionAnswerSerializers(categories, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = QuestionAnswerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    