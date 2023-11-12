from django.contrib import admin
from .models import Banner, HomeImage

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('banner_name',)}
    list_display = ('banner_name',)

admin.site.register(Banner, BannerAdmin)


class HomeImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('image_name',)}
    list_display = ('image_name',)

admin.site.register(HomeImage, HomeImageAdmin)