from django.contrib import admin
from . models import *


# Register your models here.
# admin.site.register(Search_Url)
@admin.register(URL_NOOPENER)
class With_NoOpener(admin.ModelAdmin):
    list_display=('source_url','target_url','links','noopener')

@admin.register(URL)
class Without_NoOpener(admin.ModelAdmin):
    list_display=('source_url','target_url','links')




# @admin.register(Celery_URL_NOOPENER)
# class Celery_URL_NOOPENER(admin.ModelAdmin):
#     list_display=('source_url','target_url','links','noopener')

# @admin.register(Celery_URL)
# class Celery_URL(admin.ModelAdmin):
#     list_display=('source_url','target_url','links')