# Generated by Django 3.0.2 on 2020-02-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0002_clientcredential'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipmentReference',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
