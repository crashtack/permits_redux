from django.contrib import admin
from .models import Permit, PermitOwner


# Register your models here.
admin.site.register(Permit)
admin.site.register(PermitOwner)
