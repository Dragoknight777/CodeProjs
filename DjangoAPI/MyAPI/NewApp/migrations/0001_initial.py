# Generated by Django 5.0 on 2023-12-31 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('DeveloperId', models.AutoField(primary_key=True, serialize=False)),
                ('DeveloperName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('GameId', models.AutoField(primary_key=True, serialize=False)),
                ('GameName', models.CharField(max_length=500)),
                ('GameType', models.CharField(max_length=500)),
                ('ReleaseDate', models.DateField()),
                ('GameDeveloper', models.CharField(max_length=500)),
            ],
        ),
    ]
