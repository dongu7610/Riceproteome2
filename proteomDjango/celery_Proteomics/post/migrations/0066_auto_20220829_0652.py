# Generated by Django 3.2 on 2022-08-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0065_auto_20220728_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfomodel',
            name='Change2p',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='uploadfilemodel',
            name='Change2p',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]