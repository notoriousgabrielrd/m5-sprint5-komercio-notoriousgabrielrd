from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.UserView.as_view()),
    path("login/", views.LoginUserView.as_view()),
    path("accounts/newest/<int:num>/",views.UserViewDetail.as_view())
]