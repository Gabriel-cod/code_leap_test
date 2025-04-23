from django.contrib import admin
from .models import Career


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'title', 'content', 'created_datetime')
    search_fields = ('username', 'title', 'created_datetime')
