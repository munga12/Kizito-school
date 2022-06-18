from django.contrib import admin
from django.urls import path, include

# import kizitoStudents

urlpatterns = [
    path("", include("kizitoStudents.urls")),
    path('admin/', admin.site.urls),
]
