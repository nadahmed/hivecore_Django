# Generated by Django 3.2.7 on 2021-09-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='details',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phNumber1',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phNumber2',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
