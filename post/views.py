from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello!its my project')
def current_date_view(request):
    if request.method == 'GET':
        now = timezone.localtime(timezone.now())
        return HttpResponse(now.strftime("%Y-%m-%d"))

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")