
from django.db import models
import uuid

from django.db.models.expressions import F
#from django.db.models.fields import DateTimeField
from users.models import User
#from datetime import datetime,timedelta





# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id')
    student_name = models.CharField(max_length=30,null=False)
    phone = models.CharField(max_length=12 ,null=False)



class BookModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_addbook = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_addbook')
    bookname = models.CharField(max_length=50,unique=True)
    subject = models.CharField(max_length=20,null=True)
    quantity = models.IntegerField(null=False)
    
    


  
class IssueBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_issuebook = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_issuebook')
    bookid2 = models.ForeignKey(BookModel, on_delete=models.CASCADE,related_name='bookid2')
    current_date = models.DateField(null=True, blank=False)
    expiry_date = models.DateField(null=True, blank=False)
    
    


class ReturnBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_returnbook = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_returnbook')
    issuebook_id = models.ForeignKey(IssueBook, on_delete=models.CASCADE,related_name='issuebook_id')
    

