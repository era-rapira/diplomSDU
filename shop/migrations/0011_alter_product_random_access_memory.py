# Generated by Django 3.2 on 2021-05-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210510_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='random_access_memory',
            field=models.CharField(max_length=255, null=True, verbose_name='RAM'),
        ),
    ]
