from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post.views import hello_view, current_date_view, goodbye_view, product_list_view, main_view, category_view,\
    product_detail_view, product_create_view, add_review_view
from user.views import register_view,profile_view,login_view,logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view, name='hello'),
    path('current_date/', current_date_view, name='date'),
    path('goodbye/', goodbye_view, name='goodbye'),
    path('products/', product_list_view, name='product_list'),
    path('', main_view, name='main'),
    path('category/', category_view, name='category'),
    path('products/<int:product_id>', product_detail_view, name='product_detail'),
    path('products/create/', product_create_view, name='product_create'),
    path('products/<int:product_id>/add/', add_review_view, name='add_review'),
    path('auth/register/', register_view, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('auth/profile/', profile_view, name='profile')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
