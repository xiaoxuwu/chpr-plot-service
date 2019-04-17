from django.db import models

# Create your models here.
class PlotMetadata(models.Model):
    TYPES = (
        ("DP", "Demography Pie"),
        ("DB", "Demography Bar"),
    )

    name = models.CharField(max_length=256)
    raw_data = models.FileField(upload_to='uploads/')
    orig_raw_data_filename = models.CharField(max_length=128)
    processed_data = models.FileField(upload_to='processed/')
    staff_only = models.BooleanField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    data_type = models.CharField(
        max_length=2,
        choices=TYPES,
        default="DP",
    )

    def __str__(self):
        return self.name