from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","username","phone_number",]
    list_filter = ["address",]
    search_fields = ["username","first_name","last_name","date_birth",]



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","author","published_date","price","language","created_at","is_active",]
    list_filter = ["language","price","title","author",]
    search_fields = ["title",'author',"price",]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","date_birth",]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","author","status","created_at",]
