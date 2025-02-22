# Generated by Django 4.2.6 on 2023-12-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivapp', '0002_colreg_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='compreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('compid', models.CharField(max_length=20)),
                ('phoneno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('lisence', models.FileField(upload_to='')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
