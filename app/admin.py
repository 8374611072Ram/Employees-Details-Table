from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Location)
admin.site.register(Job)
admin.site.register(Department)
admin.site.register(Employee)


