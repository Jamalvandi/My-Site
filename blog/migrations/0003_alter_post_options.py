# Generated by Django 3.2.25 on 2024-12-31 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20241230_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date']},
        ),
    ]
