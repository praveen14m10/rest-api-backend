from django.db import models
from django.contrib.auth.models import User

class RegistrationDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(null=True, blank=True)  # Add any additional fields you need

    def __str__(self):
        return self.user.username
 
 
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
 
    def __str__(self):
        return self.title
    
class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
