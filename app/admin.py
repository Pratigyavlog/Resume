from django.contrib import admin
from .models import Contact, Project, About
# Register your models here.
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(About)