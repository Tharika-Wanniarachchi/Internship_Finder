# Generated by Django 5.0.2 on 2024-02-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_company_mobilenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
        migrations.AddField(
            model_name='company',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
