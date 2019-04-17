from django.contrib import admin
from .models import PlotMetadata

class PlotMetadataAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlotMetadata, PlotMetadataAdmin)