
from rest_framework import serializers, status
from rest_framework.response import Response

from libraryApp.models import  BookModel, IssueBook, ReturnBook, Student
from users.models import User

class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)
    class Meta:
        model = Student
        fields = [
            "id",
            "user_id",
            "student_name",
            "phone",
            "password"
        ]
           
    def create(self, validated_data):
        user = User()
        
        user.username = validated_data["student_name"]
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        student = Student()
        student.student_name = validated_data["student_name"]
        student.phone = validated_data["phone"]
        student.user_id = user
        student.save()
      
        return student
    
   


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'




class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = '__all__'




class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnBook
        fields = '__all__'




