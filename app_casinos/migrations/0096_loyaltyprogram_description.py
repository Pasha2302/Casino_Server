# Generated by Django 5.0.7 on 2024-08-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0095_rename_casino_likes_casino_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltyprogram',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
