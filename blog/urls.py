from django.contrib import admin
from django.urls import path
from post.views import hello_view,current_date_view,goodbye_view,product_list_view,main_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_view,name='hello'),
    path('current_date/', current_date_view,name='date'),
    path('goodbye/', goodbye_view,name='goodbye'),
    path('products/', product_list_view,name='product_list'),
    path('', main_view, name='main')
]
