from django.contrib import admin
from .models import Project, Image, Language, Contact, Service, Skill

# Register your models here.
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Skill)
