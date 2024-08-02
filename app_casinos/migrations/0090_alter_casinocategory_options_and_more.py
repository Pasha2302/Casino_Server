# Generated by Django 5.0.7 on 2024-08-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0089_alter_payoutspeed_options_casino_review_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casinocategory',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='casinotheme',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='casino',
            name='what_we_dont_like',
            field=models.TextField(blank=True, verbose_name="What we don't like"),
        ),
        migrations.AddField(
            model_name='casino',
            name='what_we_like',
            field=models.TextField(blank=True, verbose_name='What we like'),
        ),
        migrations.AddField(
            model_name='gametype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='game_type_images/', verbose_name='Game Type Image'),
        ),
        migrations.AddField(
            model_name='language',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='language_images/', verbose_name='Language Image'),
        ),
        migrations.AddField(
            model_name='provider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='provider_images/', verbose_name='Provider Image'),
        ),
    ]
