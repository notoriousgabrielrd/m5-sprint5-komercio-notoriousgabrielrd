from dataclasses import field
from rest_framework import serializers
from products.models import ProductsModel
from users.serializer import UserSerializer

class PostProductsSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only = True)
    class Meta:
        model           = ProductsModel
        fields          = ["id","description","price","quantity","is_active","seller"]
        extra_kwargs    = {"id":{"read_only":True},"is_active":{"read_only":True},"quantity":{"min_value":0}}
        # depth           = 1

class GetProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model       = ProductsModel
        # fields      = "__all__"
        fields          = ["id","description","price","quantity","is_active","seller_id"]
        read_only_fields = ["seller_id"]


