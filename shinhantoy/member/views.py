from django.shortcuts import render
from rest_framework import generics,mixins,status
from .serializers import MemberSerializer
from .models import Member
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.response import Response

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

    def put(self, request, *args, **kwargs):
        username=request.data.get('username')
        current=request.data.get('password')
        change_password=request.data.get('change_password')
        change_password_check=request.data.get('change_password_check')

        # 변경 비번 두번 확인
        if change_password!=change_password_check:
            return Response(
                 {'detail':' new password not same'},
                 status=status.HTTP_400_BAD_REQUEST,
             )
        
        # 유저가 있는 지 확인 하는 코드
        if not Member.objects.filter(username=username).exists():
            return Response(
                 {'detail':'no account'},
                 status=status.HTTP_404_NOT_FOUND,
            )

        # 유저 찾기
        member=Member.objects.get(username=username)

        if not check_password(current,member.password):
            return Response(
                {'detail':'wrong password'},
                status=status.HTTP_400_BAD_REQUEST,
           )

       
        member.password=make_password(change_password)
        member.save()

        return Response({'detail':'good!'},status=status.HTTP_200_OK)
