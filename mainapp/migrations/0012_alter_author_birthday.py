# Generated by Django 3.2.13 on 2022-06-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20220618_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]