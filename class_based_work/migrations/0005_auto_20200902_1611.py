# Generated by Django 3.1 on 2020-09-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_based_work', '0004_auto_20200902_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
