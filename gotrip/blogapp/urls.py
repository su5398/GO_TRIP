from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from blogapp.views import blog, write, detail, search

app_name = "blogapp"

urlpatterns = [
    path('', blog, name='blog'),
    path('write/', write, name='write'),
    path('detail/<int:blog_id>', detail, name='detail'),
    path('search', search, name='search'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)