# Generated by Django 4.2.7 on 2024-01-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivapp', '0014_rename_category_comppro_collegename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegedept',
            name='status',
            field=models.CharField(default=44, max_length=20),
            preserve_default=False,
        ),
    ]
