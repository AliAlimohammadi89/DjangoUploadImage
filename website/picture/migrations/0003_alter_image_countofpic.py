# Generated by Django 4.0.4 on 2022-05-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_remove_image_title_image_countofpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='countofpic',
            field=models.IntegerField(default=3, max_length=50000, verbose_name='cont of pictors '),
        ),
    ]
