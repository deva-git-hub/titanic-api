from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:age>/<int:sex>/<int:clas>', views.show, name="show")

]
