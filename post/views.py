from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from post.models import Product, Category, Tag, Review
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
    return render(request, 'product/product_list.html', {'products': products})
def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    #review = Review
    context = {'product': product}

    return render(request, 'product/product_detail.html', context)
def category_view(request, category_id):
    category = Category.objects.get(pk=category_id)
    products_in_category = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products_in_category})
