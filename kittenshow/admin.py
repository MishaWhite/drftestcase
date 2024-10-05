from django.contrib import admin

from kittenshow.models import Kitten


# Register your models here.

@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    pass

