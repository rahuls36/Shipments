# Generated by Django 3.0.2 on 2020-02-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0006_auto_20200203_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='latestDeliveryDate',
            field=models.DateTimeField(null=True),
        ),
    ]