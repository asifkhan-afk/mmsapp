# Generated by Django 3.2.9 on 2022-09-22 16:28

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_monthrevenue_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.PositiveIntegerField(blank=True, default=22, null=True),
        ),
        migrations.AlterField(
            model_name='muqtadi',
            name='admission_date',
            field=models.IntegerField(default=22, validators=[app.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='sidefund',
            name='date',
            field=models.PositiveIntegerField(blank=True, default=22, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cnic',
            field=models.PositiveIntegerField(blank=True, max_length=15, null=True, validators=[app.validators.validate_cnic]),
        ),
    ]