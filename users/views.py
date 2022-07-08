from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from users.models import User

from users.serializer import LoginSerializer,UserSerializer

class UserView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     serializer.save()



class LoginUserView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username = serializer.validated_data["email"],
            password = serializer.validated_data["password"]
            )

        if user: 
            token,_ = Token.objects.get_or_create(user=user)
            
            return Response({"token": token.key})
        
        return Response(
            {"detail": "Invalid email or password, I can't say..."},
            status=status.HTTP_401_UNAUTHORIZED
        )



class UserViewDetail(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   
    def get_queryset(self):
        max_users = self.kwargs["num"]

        return self.queryset.order_by("-id")[0:max_users]