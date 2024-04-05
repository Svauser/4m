from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from post.models import Product, Category,Tag
from post.forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
    search=request.GET.get('search')
    sort = request.GET.get('sort', 'created_at')
    tag = request.GET.get('tag')
    page = request.GET.get('page', 1)
    products = Product.objects.all()
    if search:
        products = products.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    products = products.order_by(sort)
    limit = 3
    start = (int(page) - 1) * limit
    end = int(page) * limit

    all_pages = len(products) / limit
    if round(all_pages) < all_pages:
        all_pages += 1
    all_pages = round(all_pages)

    tags = Tag.objects.all()
    context = {
        'products': products[start:end],
        'tags': tags,
        'all_pages': range(1, all_pages + 1)
    }
    return render(request, 'product/product_list.html', context)
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
    return render(request, 'product/category.html', {'category': category, 'products': products_in_category})

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

def product_change_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'product/product_change.html', {'form': form})
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if not form.is_valid():
            return render(request, 'product/product_change.html', {'form': form})

        form.save()
        return redirect('product_list')

def product_delete_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    product.delete()
    return redirect('product_list')
