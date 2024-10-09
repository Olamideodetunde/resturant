from django.contrib import admin
from .models import News,Reservation,Menu,Contact
# Register your models here.
admin.site.register(News)
admin.site.register(Reservation)
admin.site.register(Menu)
admin.site.register(Contact)
