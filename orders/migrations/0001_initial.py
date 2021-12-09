# Generated by Django 3.2.9 on 2021-12-07 11:18

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SMALL', 'small'), ('MEDIUM', 'medium'), ('LARGE', 'large'), ('EXTRA_LARGE', 'extra_large')], default='SMALL', max_length=20)),
                ('order_status', models.CharField(choices=[('PENDING', 'pending'), ('IN_TRANSIT', 'inTransit'), ('DELIVERED', 'delivered')], default='PENDING', max_length=20)),
                ('quantity', models.IntegerField()),
                ('created_by', models.DateField(auto_now_add=True)),
                ('updated_by', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
