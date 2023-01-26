from django.shortcuts import render
from rest_framework import generics,mixins,status
from .serializers import MemberSerializer
from .models import Member
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class=MemberSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberChangePasswordView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):

    serializer_class=MemberSerializer
    #로그인한 사용자만 들어올수 있는 API가 됨
    # request.user 가 있음
    permission_classes=[IsAuthenticated]

    def put(self, request, *args, **kwargs):
        current=request.data.get('password')
        change_password=request.data.get('change_password')
        change_password_check=request.data.get('change_password_check')

        # 변경 비번 두번 확인
        if change_password!=change_password_check:
            return Response(
                 {'detail':' new password not same'},
                 status=status.HTTP_400_BAD_REQUEST,
             )
        
        member=request.user

        if not check_password(current,member.password):
            return Response(
                {'detail':'wrong password'},
                status=status.HTTP_400_BAD_REQUEST,
           )

       
        member.password=make_password(change_password)
        member.save()

        return Response({'detail':'good!'},status=status.HTTP_200_OK)
