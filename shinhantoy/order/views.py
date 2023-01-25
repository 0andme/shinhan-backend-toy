from django.shortcuts import render
from rest_framework import generics,mixins
from .serializer import OrderSerializer
from .models import Order
# Create your views here.


class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):

    serializer_class=OrderSerializer
    def get_queryset(self):

        orders=Order.objects.all().order_by('id')

        return  orders

    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)
  