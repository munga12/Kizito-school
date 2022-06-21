from . import views
from django.urls import path

# the foward slash should always come after the url name

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("", views.home, name="home")
]