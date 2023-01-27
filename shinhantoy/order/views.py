from django.shortcuts import render
from rest_framework import generics,mixins
from .serializer import OrderSerializer,CommentSerializer,CommentCreateSerializer
from .models import Order,Comment
from rest_framework.permissions import IsAuthenticated

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):

    serializer_class=OrderSerializer
    def get_queryset(self):
        return  Order.objects.all().order_by('-id')

    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):

    serializer_class=OrderSerializer
    def get_queryset(self):
      
        return Order.objects.all().order_by('-id')

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,args,kwargs)


class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class=CommentSerializer
    def get_queryset(self):
        searchword=self.request.query_params.get('search')
        order_id=self.kwargs.get('pk')
        if(order_id):
            if(searchword):
                return Comment.objects.filter( order_id=order_id , content__contains=searchword).order_by('-id')
            return Comment.objects.filter(order_id=order_id).order_by('-id')
        return Comment.objects.none()

    def get(self,request,*args,**kwargs):
       return self.list(request,args,kwargs)
    

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class=CommentCreateSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class CommentDetailView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)