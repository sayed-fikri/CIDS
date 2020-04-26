from django.contrib import admin
from .models import Page, Annoucement

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class AnnoucementAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Page, PageAdmin)
admin.site.register(Annoucement, AnnoucementAdmin)

# Register your models here.
