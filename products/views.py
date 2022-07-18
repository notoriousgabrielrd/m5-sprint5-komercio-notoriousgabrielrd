from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from . import serializer
from . import utils
from . import models
from . import permissions

class ProductsView(utils.SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.MyCustomPermission,permissions.isSeller]

    queryset = models.ProductsModel.objects.all()
    serializer_map = {"GET":serializer.GetProductsSerializer, "POST":serializer.PostProductsSerializer}
    

    def perform_create(self, serializer):

        print(type(self.request.user))
        print(self.request.user)

        serializer.save(seller = self.request.user)


class ProductsDetailView(utils.SerializerByMethodMixin,generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwner,permissions.MyCustomPermission]

    queryset = models.ProductsModel.objects.all()    
    serializer_map = {"GET":serializer.GetProductsSerializer, "PATCH":serializer.PostProductsSerializer}
