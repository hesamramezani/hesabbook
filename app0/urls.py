from django.urls import path
from app0.views import Expend_views , Income_views

urlpatterns = [
    path("expend/" , Expend_views.as_view() , name = "expend"),
    path("income/" , Income_views.as_view() , name = "income"),

]
