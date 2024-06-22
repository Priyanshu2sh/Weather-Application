from django.contrib import admin
from .models import City

# Register the City model with the Django admin site
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view of the City model in the admin site
    list_display = ['id','name']