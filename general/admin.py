from django.contrib import admin
from general import models
from general.models import ContactModel,loginModel

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(loginModel)
