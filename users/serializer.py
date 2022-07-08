from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model        = models.User
        fields       = ["id","email","password","first_name","last_name","is_seller","date_joined"]
        extra_kwargs = {"password":{"write_only":True}, "date_joined":{"read_only":True},"id":{"read_only":True}} 


    def validate_email(self,value):
        if models.User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists!")

        return value


    def create(self,validated_data:dict) -> models.User:
        return models.User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)
