from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.db.models import F
from libraryApp.models import BookModel, IssueBook, ReturnBook, Student
from .serailizers import BookModelSerializer, IssueBookSerializer, ReturnBookSerializer, StudentSerializer
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication


class BookView(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["admin"]
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer


class StudentView(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["student"]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   

class IssueBookView(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["student"]
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer    
    def create(self,request):
        book = BookModel.objects.filter(id=request.data['bookid2'])
        for i in book:
            if i.quantity != 0:
                i.quantity = i.quantity - 1
                BookModel.objects.filter(id=request.data['bookid2']).update(quantity=i.quantity)
                super().create(request)
                return Response("Request Accepeted! ")
            else:
                return Response("book is not available...")    
        
    
    
    
class ReturnBookView(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["student"]
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer 
    def create(self,request):
        super().create(request)
        issue_book = IssueBook.objects.get(id=request.data['issuebook_id'])
        BookModel.objects.filter(id=issue_book.bookid2.id).update(quantity=F('quantity')+1)
        
        return Response("success! your Book is returned. ")               
    
   



        

   
        
    
    

    
    
             
        
        
                 
        
                
            
                


        
      
      
        
        
       

            
            
            
           