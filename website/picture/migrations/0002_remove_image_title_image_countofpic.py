# Generated by Django 4.0.4 on 2022-05-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='countofpic',
            field=models.IntegerField(default=3, max_length=200, verbose_name='cont of pictors '),
        ),
    ]