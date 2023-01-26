from django.shortcuts import render
from rest_framework import generics,mixins
from .serializers import MemberSerializer


class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class=MemberSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)