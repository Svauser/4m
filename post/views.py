from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from post.models import Product, Category
from post.forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

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
    user=request.user
    if request.method == 'GET':
        return render(request, 'main.html', {'user': user})


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

@login_required(login_url='/auth/login')
def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    context = {'product': product}

    return render(request, 'product/product_detail.html', context)


def category_view(request, category_id):
    category = Category.objects.get(pk=category_id)
    products_in_category = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products_in_category})

@login_required(login_url='/auth/login')
def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product/product_create.html', {'form': form})

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'product/product_create.html', {'form': form})

        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        image = form.cleaned_data.get('image')
        price = form.cleaned_data.get('price')
        category = form.cleaned_data.get('category')
        tags = form.cleaned_data.get('tags')

        product = Product.objects.create(
            name=name,
            description=description,
            image=image,
            price=price,
            user=request.user
        )

        product.tags.set(tags)
        product.category = category
        product.save()
        return redirect('product_list')

def add_review_view(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'product/add_review.html', {'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
        else:
            return render(request, 'product/add_review.html', {'form': form})