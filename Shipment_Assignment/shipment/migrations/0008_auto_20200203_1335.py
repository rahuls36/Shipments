# Generated by Django 3.0.2 on 2020-02-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0007_auto_20200203_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ean',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderItemId',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipmentId',
            field=models.BigIntegerField(),
        ),
    ]
