from django.urls import path
from post.views import hello_view,current_date_view,goodbye_view,\
    product_list_view,main_view,category_view,product_detail_view,\
    product_create_view,add_review_view,product_change_view,product_delete_view,\
    HelloView,ProductListView,ProductCreateView,ProductDetailView,ProductUpdateView,\
    ProductDeleteView
urlpatterns = [
    path('', main_view, name='main'),
    path('hello/', hello_view, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('current_date/', current_date_view, name='date'),
    path('goodbye/', goodbye_view, name='goodbye'),
    path('products/', product_list_view, name='product_list'),
    path('products2/', ProductListView.as_view, name='product_list2'),
    path('category/', category_view, name='category'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products2/<int:product_id>/', ProductDetailView.as_view, name='product_list2'),
    path('products/create/', product_create_view, name='product_create'),
    path('products2/create/', ProductCreateView.as_view, name='product_create2'),
    path('products/<int:product_id>/add/', add_review_view, name='add_review'),
    path('products/<int:product_id>/update/', product_change_view, name='product_edit'),
    path('products2/<int:product_id>/update/', ProductUpdateView.as_view, name='product_edit2'),
    path('products/<int:product_id>/delete/', product_delete_view, name='product_delete'),
    path('products2/<int:product_id>/delete/', ProductDeleteView.as_view, name='product_delete2')
]