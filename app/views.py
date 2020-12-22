

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle
from sklearn.linear_model import LogisticRegression

# Create your views here.


def index(request):
    return render(request, "index.html", {"value": "Yes"})


def show(request, age, sex, clas):
    age = float(age)
    sex = float(sex)
    clas = float(clas)
    model = pickle.load(open("LRmodel", 'rb'))
    e = 2.71828
    coeff = model.coef_
    inter = model.intercept_
    val = 1/(1+pow(e, -(coeff[0][0]*int(age)+coeff[0]
                        [1]*int(sex)+coeff[0][2]*int(clas) + inter)))
    val = val*100
   
    return HttpResponse(val)


class showData(APIView):
    def get(self, request):
        return (" Hello")

    def post(self, request):
        pass
