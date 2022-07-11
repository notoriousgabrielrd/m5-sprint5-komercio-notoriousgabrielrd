from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework.generics import ListCreateAPIView,ListAPIView, UpdateAPIView,RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from users.models import User
from users.permissions import IsOwner, IsSuperUserPermission

from users.serializer import LoginSerializer, SuperUserUpdateSerializer,UserSerializer, UserUpdateSerializer

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



class UserUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]


    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class SuperUserUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserPermission]


    queryset = User.objects.all()
    serializer_class = SuperUserUpdateSerializer

