# Generated by Django 3.2.9 on 2022-09-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220916_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidefund',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]