# Generated by Django 5.0 on 2024-11-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.ManyToManyField(related_name='user', to='apis.groups'),
        ),
    ]
