# Generated by Django 2.2.1 on 2019-05-31 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0008_auto_20190531_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblock',
            name='chart',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='internal.PlotMetadata'),
        ),
    ]
