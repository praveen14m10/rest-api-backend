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
import pandas as pd
from django.conf import settings
import os
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

    def perform_create(self, serializer):
        file = self.request.FILES['file']
        # Save the file instance
        file_instance = serializer.save()
        
        # Determine file type and read the file
        file_path = os.path.join(settings.MEDIA_ROOT, file_instance.file.name)
        if file.name.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file.name.endswith('.ods'):
            df = pd.read_excel(file_path, engine='odf')
        else:
            raise ValueError('Unsupported file type')

        # Iterate over each row and create a new FileUpload instance for each
        for index, row in df.iterrows():
            first_name = row.get('First Name', '')
            last_name = row.get('Last Name', '')
            email = row.get('Email', '')

            # Create a new FileUpload instance for each row
            FileUpload.objects.create(
                file=file_instance.file,  # Use the same file for all instances
                first_name=first_name,
                last_name=last_name,
                email=email
            )
        
        # Optionally, delete the initial file_instance if it's not needed
        file_instance.delete()
        
class FileUploadListView(generics.ListAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer