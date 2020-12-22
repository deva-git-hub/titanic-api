from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<str:age>/<str:sex>/<str:clas>', views.show, name="show")

]
