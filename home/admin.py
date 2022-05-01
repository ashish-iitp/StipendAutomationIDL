from django.contrib import admin
from .models import *
# Register your models here.

class EMPLOYEES(admin.ModelAdmin):
    change_list_template = 'new_template.html'

admin.site.register(Employee, EMPLOYEES)
admin.site.register(RndAdmin)
admin.site.register(Faculty)