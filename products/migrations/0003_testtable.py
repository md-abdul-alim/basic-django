# Generated by Django 3.1 on 2020-09-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=120)),
            ],
        ),
    ]
