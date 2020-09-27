from django.contrib import admin
from .models import Employee,CompanyHead,TopEmployee
# Register your models here.

admin.site.register(Employee)
admin.site.register(CompanyHead)
admin.site.register(TopEmployee)