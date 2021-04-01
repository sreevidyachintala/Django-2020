# Generated by Django 3.0.5 on 2020-04-29 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.CharField(max_length=20)),
                ('stuName', models.CharField(max_length=30)),
                ('branch', models.CharField(choices=[('CSE', 'cse'), ('ECE', 'ece'), ('MEC', 'mec'), ('EEE', 'eee'), ('IT', 'it')], max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
