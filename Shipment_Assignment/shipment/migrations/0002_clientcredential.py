# Generated by Django 3.0.2 on 2020-02-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=1024)),
                ('client_secret', models.CharField(max_length=4096)),
            ],
        ),
    ]
