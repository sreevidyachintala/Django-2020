# Generated by Django 3.0.4 on 2020-04-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
