from django.contrib import admin

# Register your models here.
from .models import Trait, Population

admin.site.register(Trait)
admin.site.register(Population)