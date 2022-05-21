from django.shortcuts import render
from .serializer import Expend_serializer , Income_serializer , User_serializer
from .models import Expend , Income
from rest_framework.generics import CreateAPIView , ListAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.db.models import Sum, Count
from rest_framework import status
from app0.permission import IsSuperUser , IsOwner
from rest_framework.permissions import IsAuthenticated


class Create_user(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer


class User_list(ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer
    permission_classes = (IsSuperUser ,)


class Expend_views(CreateAPIView):
    queryset = Expend.objects.all()
    serializer_class = Expend_serializer
    permission_classes = (IsAuthenticated ,)


class Edit_expend(APIView):
    permission_classes = (IsOwner ,)

    def get(self , request , pk):
        queryset = Expend.objects.all().filter(user_id=pk)
        serialize = Expend_serializer(queryset , many=True)
        return Response(serialize.data)

    def put(self , request , pk):
        queryset = Expend.objects.get(pk = pk)
        serializer = Expend_serializer(queryset , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self , request , pk):
        queryset = Expend.objects.get(pk = pk)
        queryset.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class Income_views(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = Income_serializer
    permission_classes = (IsAuthenticated ,)


class Edit_income(APIView):
    permission_classes = (IsOwner ,)

    def get(self , request , pk):
        queryset = Income.objects.all().filter(user_id=pk)
        serialize = Income_serializer(queryset , many=True)
        return Response(serialize.data)

    def put(self , request , pk):
        queryset = Income.objects.get(pk = pk)
        serializer = Income_serializer(queryset , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self , request , pk):
        queryset = Income.objects.get(pk = pk)
        queryset.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



class Sum_of_Expend(APIView):
    permission_classes = (IsOwner,)

    def get(self , request , pk):
        queyset = User.objects.get(pk = pk)
        return Response(Expend.objects.filter(user=queyset).aggregate(Count("amount") , Sum("amount")))



class Sum_of_Income(APIView):
    permission_classes = (IsOwner,)

    def get(self , request , pk):
        queyset = User.objects.get(pk = pk)
        return Response(Income.objects.filter(user=queyset).aggregate(Count("amount") , Sum("amount")))



