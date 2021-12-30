# Generated by Django 3.2.8 on 2021-12-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaptopApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='Processor',
            new_name='processor',
        ),
        migrations.AddField(
            model_name='laptop',
            name='document',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='laptop',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
