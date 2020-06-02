from django.contrib import admin
from .models import Enquiry, Events, Options, Transactions

admin.site.register(Enquiry)
admin.site.register(Events)
admin.site.register(Options)
admin.site.register(Transactions)