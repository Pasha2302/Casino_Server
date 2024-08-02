# Generated by Django 5.0.7 on 2024-08-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casinos', '0094_bonus_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casino',
            old_name='casino_likes',
            new_name='likes',
        ),
        migrations.AddField(
            model_name='loyaltyprogram',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Loyalty Likes'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='bonuses/files/', verbose_name='File Path'),
        ),
    ]
