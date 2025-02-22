# Generated by Django 5.0 on 2024-01-03 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivapp', '0009_cabout_comppro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabout',
            old_name='name',
            new_name='tname',
        ),
        migrations.RenameField(
            model_name='comppro',
            old_name='name',
            new_name='tname',
        ),
        migrations.AddField(
            model_name='cabout',
            name='cname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ivapp.compreg'),
        ),
        migrations.AddField(
            model_name='comppro',
            name='cname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ivapp.compreg'),
        ),
    ]
