# Generated by Django 2.2.6 on 2020-04-22 14:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_mldata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busapidata',
            name='shortname',
        ),
        migrations.RemoveField(
            model_name='busapidata',
            name='stopid',
        ),
        migrations.AddField(
            model_name='busapidata',
            name='location_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='busapidata',
            name='routes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256, null=True), null=True, size=20),
        ),
        migrations.AddField(
            model_name='busapidata',
            name='stop_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='busapidata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='busapidata',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='busapidata',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='busapidata',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=16, null=True),
        ),
    ]
