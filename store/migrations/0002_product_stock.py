# Generated by Django 5.1.3 on 2025-03-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Остаток на складе'),
        ),
    ]
