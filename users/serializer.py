from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model        = models.User
        fields       = ["id","email","password","first_name","last_name","is_seller","date_joined","is_active"]
        extra_kwargs = {"password":{"write_only":True}, "date_joined":{"read_only":True},"id":{"read_only":True},"is_active":{"read_only":True}} 


    def validate_email(self,value):
        if models.User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists!")

        return value


    def create(self,validated_data:dict) -> models.User:
        return models.User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model        = models.User
        fields       = ["id","email","password","first_name","last_name","is_seller","date_joined","is_active"]
        extra_kwargs = {"password":{"write_only":True}, "date_joined":{"read_only":True},"id":{"read_only":True},"is_active":{"read_only":True}} 

    def update(self, instance:models.User, validated_data:dict):

        non_editable_keys = ("is_active")

        for key, value in validated_data.items():
            if key in non_editable_keys:
                raise KeyError
            setattr(instance, key, value)

        instance.save()

        return instance


class SuperUserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model        = models.User
        fields       = ["is_active"]
        # extra_kwargs = {"password":{"write_only":True}, "date_joined":{"read_only":True},"id":{"read_only":True},"is_active":{"read_only":True}} 
