# Generated by Django 3.2.9 on 2021-12-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
