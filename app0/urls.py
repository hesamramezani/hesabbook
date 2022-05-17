from django.urls import path
from app0.views import Expend_views , Income_views , Sum_of_Expend , Sum_of_Income

urlpatterns = [
    path("expend/" , Expend_views.as_view() , name = "expend"),
    path("income/" , Income_views.as_view() , name = "income"),
    path("sumofexpend/<int:pk>/" , Sum_of_Expend.as_view() , name = "Sum_of_Expend"),
    path("sumofincome/<int:pk>/", Sum_of_Income.as_view(), name="Sum_of_Income"),

]
