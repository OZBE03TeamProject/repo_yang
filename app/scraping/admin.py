from django.contrib import admin
from scraping.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant_name",
        "restaurant_address",
        "review_count",
        "category",
        "star_rate",
        "thumbnail_image",
        "current_state",
        "phone_number",
    )
