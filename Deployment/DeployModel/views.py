import joblib
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request, 'index.html')

def result(request):

    cls = joblib.load('C:\Projects\Machine_learning_App_with_Django\model.sav')

    li =[]

    li.append(request.GET['RI'])
    li.append(request.GET['Na'])
    li.append(request.GET['Mg'])
    li.append(request.GET['Al'])
    li.append(request.GET['Si'])
    li.append(request.GET['K'])
    li.append(request.GET['Ca'])
    li.append(request.GET['Ba'])
    li.append(request.GET['Fe'])

    print(li)

    res = cls.predict([li])


    return render (request, 'result.html',{'res':res,'li':li})
