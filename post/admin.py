from django.contrib import admin

from post.models import Product, Review, Tag, Category
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['name']
    readonly_fields = ('created_at', 'updated_at','id')
    # fieldsets = (
    #     (
    #         None, {
    #             'fields':('name','category','tags','price')
    #         }),
    #     (
    #         'Readonly Fields',{
    #             'fields':('id','created_at','updated_at'),
    #             'classes':('collapse',)
    #         }
    #     )
    #
    # )
    def save_model(self, request, obj, form, change):
        obj.name = obj.name.capitalize()
        super().save_model(request,obj,form,change)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product','text','created_at')
admin.site.register(Tag)
admin.site.register(Category)