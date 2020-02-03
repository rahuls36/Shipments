from django.db import models

# Create your models here.

class ClientCredential(models.Model):
    client_id = models.CharField(max_length = 1024)
    client_secret = models.CharField(max_length = 4096)

    def __str__(self):
        return self.client_id


class Shipment(models.Model):
    shipmentId = models.BigIntegerField()
    shipmentDate = models.DateTimeField()

    def __str__(self):
        return self.shipmentId


class Order(models.Model):
    orderItemId = models.BigIntegerField(blank = True, null = True)
    orderId = models.BigIntegerField(primary_key= True)
    orderDate = models.DateTimeField(blank = True, null = True)
    latestDeliveryDate = models.DateTimeField(null = True)
    ean = models.BigIntegerField(blank = True,null = True)
    title = models.CharField(max_length = 4096,null = True)
    quantity = models.BigIntegerField(blank = True,null = True)
    offerPrice = models.FloatField(blank = True,null = True)
    offerCondition = models.CharField(max_length= 1024,null = True)
    fulfilmentMethod = models.CharField(max_length = 1024,null = True)
    shipment = models.ForeignKey(Shipment, on_delete= models.CASCADE, related_name= "order")

    def __str__(self):
        return str(self.orderId)



