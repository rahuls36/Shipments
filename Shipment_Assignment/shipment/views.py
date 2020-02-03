from django.shortcuts import render
from rest_framework.views import APIView
from .models import Shipment,ClientCredential, Order
from .serializers import ShipmentSerializer,ClientCredentialSerializer,OrderSerializer
import requests
from rest_framework import status
from rest_framework.response import Response
import sched, time
from threading import Timer
import os

s = sched.scheduler(time.time, time.sleep)
import json

# Create your views here.

class ClientCredentialView(APIView):
    def get(self, request):
        clientCredential = ClientCredential.objects.all()
        serializer = ClientCredentialSerializer(clientCredential, many= True)
        return Response(serializer.data)

    def post(self,request):
        clientCredential = ClientCredentialSerializer(data = request.data)
        if clientCredential.is_valid():
            clientCredential.save()
            resp = Response(clientCredential.data, status=status.HTTP_201_CREATED)
            return resp
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class ShipmentView(APIView):

    access_token = ""

    def get_access_token(self, creds):
        '''

        :param creds: The Credentials of the user
        :return: None
        '''
        response = requests.post('https://login.bol.com/token?grant_type=client_credentials',
                                 headers={"Content-Type": "application/x-www-form-urlencoded",
                                          "Accept": "application/json"},
                                 data={
                                     "client_id": creds.client_id,
                                     "client_secret": creds.client_secret
                                 })
        json_response = response.json()
        global access_token
        access_token = json_response["access_token"]

    def get(self, request, *args, **kwargs):
        '''

        :param request: The request Object
        :param args:
        :param kwargs:
        :return:
        List of Shipments
        '''
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many = True)
        return Response(serializer.data)

    def post(self,request):
        creds = ClientCredential.objects.get(pk = 1)
        Timer(250, self.get_access_token(creds),()).start()
        time.sleep(2)
        bearer_token = "Bearer {}".format(access_token)
        headers = {
            "Authorization" : bearer_token,
            "Accept": "application/vnd.retailer.v3+json"
        }
        for fulfilment_method in ['FBR','FBB']:
            ## Get the Shipments
            response = requests.get("https://api.bol.com/retailer/shipments",
                                    params = {"fulfilment-method" : fulfilment_method },
                                    headers = headers)
            shipments = response.json().get('shipments',[])

            for shipment in shipments:
                shipment_id = shipment.get('shipmentId')
                if shipment_id:
                    response = requests.get("https://api.bol.com/retailer/shipments/{}".format(int(shipment_id)),
                                        headers=headers)

                    shipment_obj = response.json()
                    shipment_to_add = {
                        "shipmentId" : shipment_obj.get('shipmentId'),
                        "shipmentDate": shipment_obj.get('shipmentDate'),
                    }
                    try:
                        ship = Shipment.objects.get(pk=int(shipment_obj.get('shipmentId')))
                        ship.delete()
                    except Exception as e:
                        pass
                    ship = Shipment.objects.create(**shipment_to_add)
                    for order in shipment_obj.get('shipmentItems'):
                        try:
                            order_obj = Order.objects.get(pk = int(order.get('orderId')))
                            order_obj.delete()
                        except Exception as e:
                            pass
                        Order.objects.create(orderId= order.get('orderId'), orderItemId = order.get('orderItemId'),
                                             orderDate = order.get('orderDate'),latestDeliveryDate = order.get('latestDeliveryDate'),
                                             ean = order.get('ean'),title = order.get('title'), quantity = order.get('quantity'),
                                             offerPrice = order.get('offerPrice'),offerCondition = order.get('offerCondition'),
                                             fulfilmentMethod = order.get('fulfilmentMethod'),shipment = ship)
                    time.sleep(10)

        return Response({"status": "Synced Shipments"}, status=status.HTTP_201_CREATED)

class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        shipments = Order.objects.all()
        serializer = OrderSerializer(shipments, many = True)
        return Response(serializer.data)




