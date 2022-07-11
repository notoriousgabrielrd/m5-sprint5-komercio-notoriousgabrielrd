from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.ProductsView.as_view()),
    path("products/<int:pk>/", views.ProductsDetailView.as_view())
]
