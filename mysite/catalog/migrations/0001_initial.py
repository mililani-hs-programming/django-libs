# Generated by Django 3.1.2 on 2020-10-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Input', models.CharField(max_length=500)),
                ('Ouput', models.CharField(max_length=500)),
            ],
        ),
    ]
