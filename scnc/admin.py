from django.contrib import admin
from .models import Cnc
# Register your models here.
class CncAdmin(admin.ModelAdmin):
    list_display = ('topic', 'image', 'decs', 'file', 'date')

admin.site.register(Cnc,CncAdmin)