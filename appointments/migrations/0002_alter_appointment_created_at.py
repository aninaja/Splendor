# Generated by Django 4.2.5 on 2023-12-02 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 2, 7, 18, 9, 975671)),
        ),
    ]
