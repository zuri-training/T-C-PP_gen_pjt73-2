from django.contrib import admin
from .models import Lawyer, Customer, Company, Template #Reviews,

# Register your models here.
admin.site.register(Lawyer)
admin.site.register(Customer)
# admin.site.register(Reviews)
admin.site.register(Company)
admin.site.register(Template)