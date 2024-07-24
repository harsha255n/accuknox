from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import Signup,searchuser
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserSearch(APIView):
    permission_classes = [IsAuthenticated]

class Signupview(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Signup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class search(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.GET.get("username")

        if query:
            users = User.objects.filter(username__icontains=query)
        else:
            users = User.objects.none()

        serializer = Signup(users, many=True)
        return Response(data=serializer.data)
              

