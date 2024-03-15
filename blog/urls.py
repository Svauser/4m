from django.contrib import admin
from django.urls import path
from post.views import  hello_view,current_date_view,goodbye_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_view),
    path('current_date/', current_date_view),
    path('goodbye/', goodbye_view),
]
