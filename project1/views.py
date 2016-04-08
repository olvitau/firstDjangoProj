from django.http import HttpResponse
#from django.shortcuts import render

# Create your views here.


def index(request):
    resp = u'<body>Hello!</body>'
    return HttpResponse(resp)