# Generated by Django 2.1.7 on 2019-02-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20190212_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, height_field=250, upload_to='img/item', width_field=250),
        ),
    ]