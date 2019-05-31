from django.contrib import admin
from .models import PlotMetadata, Project, ContentBlock

class PlotMetadataAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class ContentBlockAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlotMetadata, PlotMetadataAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)