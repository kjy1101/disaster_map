# Generated by Django 4.0.4 on 2022-04-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='region_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mark',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]
