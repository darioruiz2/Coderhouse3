# Generated by Django 4.1.3 on 2023-01-19 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApkFinal1', '0009_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(upload_to='avatares'),
        ),
    ]
