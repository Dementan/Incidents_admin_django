# Generated by Django 4.1.2 on 2022-10-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('incident_type', models.CharField(max_length=15)),
                ('message_sourse', models.CharField(max_length=15)),
            ],
        ),
    ]
