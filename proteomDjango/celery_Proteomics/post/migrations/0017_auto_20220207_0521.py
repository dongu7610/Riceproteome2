# Generated by Django 2.2.14 on 2022-02-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20220207_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgfieldmodel',
            name='imagefiles',
            field=models.ImageField(blank=True, null=True, upload_to='images/WholePNG'),
        ),
    ]