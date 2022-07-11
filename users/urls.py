from django.urls import path

from users.serializer import SuperUserUpdateSerializer
from . import views

urlpatterns = [
    path("accounts/", views.UserView.as_view()),
    path("login/", views.LoginUserView.as_view()),
    path("accounts/newest/<int:num>/",views.UserViewDetail.as_view()),
    path("accounts/<int:pk>/",views.UserUpdateView.as_view()),
    path("accounts/<int:pk>/management/",views.SuperUserUpdateView.as_view()),

]