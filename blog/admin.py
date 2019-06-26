from django.contrib import admin
from blog.models import Post, Category
from django.db import models

from pagedown.widgets import AdminPagedownWidget

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, PostAdmin)
