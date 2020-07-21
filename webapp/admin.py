from django.contrib import admin
from . models import Users
from . models import csvDb

admin.site.register(Users)
admin.site.register(csvDb)
