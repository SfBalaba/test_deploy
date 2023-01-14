from django.contrib import admin

from .models import Home_data, About, Buyer


@admin.register(Home_data)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    pass