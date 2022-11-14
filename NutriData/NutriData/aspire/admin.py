from django.contrib import admin
from .models import Recipe, Folder, Account


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Folder)
admin.site.register(Account)


