from django.contrib import admin
from django.db import models
from projects.models import Project

from pagedown.widgets import AdminPagedownWidget


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(Project, ProjectAdmin)
