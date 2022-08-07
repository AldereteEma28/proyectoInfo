import datetime
from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s 
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)
