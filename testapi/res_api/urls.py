from django.contrib import admin
# include necessary libraries

from django.urls import path, include
from .views import *  
from .views import RegisterView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('GeeksViewSet/',GeeksViewSet, name='GeeksViewSet'),
    path('getfile/',getfile, name='getfile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('users/', UserListView.as_view(), name='user_list'),

]
