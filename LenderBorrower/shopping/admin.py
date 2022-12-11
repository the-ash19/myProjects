from django.contrib import admin
from .models import Slot,Lender,Borrower

# Register your models here.
admin.site.register(Lender)
admin.site.register(Slot)
admin.site.register(Borrower)
