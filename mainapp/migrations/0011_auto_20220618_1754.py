# Generated by Django 3.2.13 on 2022-06-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20220616_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='birthday',
            field=models.DateField(default='2020-04-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]