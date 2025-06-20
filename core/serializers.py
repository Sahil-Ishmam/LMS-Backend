from rest_framework import serializers
from .models import Category,Course,Lesson,Material,Enrollment,QuestionAnswer


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    
         
class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    
         
class MaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    

class EnrollmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


    

class QuestionAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'

    
              