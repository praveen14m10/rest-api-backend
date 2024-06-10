from django.contrib import admin
# include necessary libraries
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    # add apis urls
    path('', include("res_api.urls"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    