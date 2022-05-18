from django.urls import path
from app0.views import Expend_views , Income_views , Sum_of_Expend , Sum_of_Income , \
    Create_user , User_list , Edit_expend , Edit_income

urlpatterns = [
    path("expend/" , Expend_views.as_view() , name = "expend"),
    path("income/" , Income_views.as_view() , name = "income"),
    path("sumofexpend/<int:pk>/" , Sum_of_Expend.as_view() , name = "Sum_of_Expend"),
    path("sumofincome/<int:pk>/", Sum_of_Income.as_view(), name="Sum_of_Income"),
    path("createuser/", Create_user.as_view(), name="Create_user"),
    path("userlist/" , User_list.as_view() , name = "User_list"),
    path("editexpend/<int:pk>/", Edit_expend.as_view(), name="Edit_expend"),
    path("editincome/<int:pk>/", Edit_income.as_view(), name="Edit_income"),

]
