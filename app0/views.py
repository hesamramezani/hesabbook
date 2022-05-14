from django.shortcuts import render
from .serializer import Expend_serializer , Income_serializer
from .models import Expend , Income
from rest_framework.generics import CreateAPIView

class Expend_views(CreateAPIView):
    queryset = Expend.objects.all()
    serializer_class = Expend_serializer


class Income_views(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = Income_serializer
