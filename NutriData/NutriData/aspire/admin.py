from django.contrib import admin
from .models import Recipe, Folder, User, Recipe_User


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Folder)
admin.site.register(User)
admin.site.register(Recipe_User)


