# Generated by Django 2.2.17 on 2020-12-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('rate', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
