from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20)
    fa_icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name

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

class ContentBlock(models.Model):
    TYPES = (
        ("H", "Title"),
        ("P", "Paragraph"),
        ("C", "Chart")
    )

    order = models.IntegerField()
    content_type = models.CharField(
        max_length=2,
        choices=TYPES,
        default="H",
    )
    text_content = models.TextField(blank=True)
    chart = models.ForeignKey(PlotMetadata, blank=True, null=True, default=None, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (order: %s) (text: %s) (chart: %s)' % (self.get_content_type_display(), self.order, self.text_content, self.chart)