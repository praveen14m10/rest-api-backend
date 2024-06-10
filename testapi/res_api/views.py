from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view

# import local data
# from .serializers import GeeksSerializer
from .models import GeeksModel
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileUpload
from .serializers import FileUploadSerializer

# create a viewset

@api_view(['GET'])
def GeeksViewSet(request):
    queryset = GeeksModel.objects.values()
    print(list(queryset),"hygtfredwq")
    return JsonResponse({"data" : list(queryset)},safe=False)
	


@api_view(['POST'])
def getfile(request):
    print(request.data)
    return JsonResponse({"data" : "new name"})

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class FileUploadView(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)