from django.contrib import admin

from .models import User,Street,City,Work


admin.site.register(City)
admin.site.register(Street)
admin.site.register(Work)
admin.site.register(User)