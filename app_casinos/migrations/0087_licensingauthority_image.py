# Generated by Django 5.0.7 on 2024-08-01 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0086_alter_casino_casino_likes_loyaltykeypoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='licensingauthority',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='licensing_authority_images/', verbose_name='Licensing Authority Image'),
        ),
    ]
