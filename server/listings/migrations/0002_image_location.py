# Generated by Django 2.1 on 2019-04-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ImageField(default=1, upload_to='listing_images'),
            preserve_default=False,
        ),
    ]
