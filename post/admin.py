from django.contrib import admin

from post.models import Product, Review, Tag, Category
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)
