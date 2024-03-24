from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from post.models import Product
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
def main_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})