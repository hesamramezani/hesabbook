from django.shortcuts import render
from .serializer import Expend_serializer , Income_serializer
from .models import Expend , Income
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.db.models import Sum, Count


class Expend_views(CreateAPIView):
    queryset = Expend.objects.all()
    serializer_class = Expend_serializer


class Income_views(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = Income_serializer


class Sum_of_Expend(APIView):
    def get(self , request , pk):
        queyset = User.objects.get(pk = pk)
        return Response(Expend.objects.filter(user=queyset).aggregate(Count("amount") , Sum("amount")))



class Sum_of_Income(APIView):
    def get(self , request , pk):
        queyset = User.objects.get(pk = pk)
        return Response(Income.objects.filter(user=queyset).aggregate(Count("amount") , Sum("amount")))
