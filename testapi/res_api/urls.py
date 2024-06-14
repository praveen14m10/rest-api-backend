from django.contrib import admin
# include necessary libraries
from django.conf import settings
from django.conf.urls.static import static
from .views import FileUploadView
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
    path('users/', UserListView.as_view(), name='user_list'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('fileuploads/', FileUploadListView.as_view(), name='fileupload-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)