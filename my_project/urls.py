from django.contrib import admin
from django.urls import path, include
from reviews import urls as reviews_urls  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(reviews_urls)),       
]
