# Generated by Django 3.0.2 on 2020-02-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0004_auto_20200203_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderItemId',
            field=models.IntegerField(blank=True, default=123456789),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='ean',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='offerPrice',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderDate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
    ]
