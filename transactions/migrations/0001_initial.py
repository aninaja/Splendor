# Generated by Django 4.2.5 on 2023-11-05 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(default=None, max_length=200, unique=True)),
                ('price_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('offer_code', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transactions',
                'unique_together': {('user', 'offer_code')},
            },
        ),
    ]
