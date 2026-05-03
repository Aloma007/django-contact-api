from django.contrib import admin
from .models import Contact

# This registers your exact database model to the dashboard
admin.site.register(Contact)