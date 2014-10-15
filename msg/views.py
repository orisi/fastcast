from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from msg.serializers import UserSerializer, GroupSerializer
from msg.models import Msg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


from msg.models import Msg
from msg.serializers import MsgSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, renderers
from rest_framework.decorators import api_view

from rest_framework import generics
from datetime import datetime, timedelta

class MsgList(generics.ListCreateAPIView):
    queryset = Msg.objects.all().order_by('-timestamp')
    serializer_class = MsgSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100




class MsgListLast(generics.ListCreateAPIView):
    backtime = datetime.now()-timedelta(minutes=240)
    now = datetime.now()+timedelta(minutes=2)

    queryset = Msg.objects.filter(timestamp__range=[backtime,now])
    serializer_class = MsgSerializer

    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    """

# here you could easily disconnect Update/Destroy functionality
class MsgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer
    
    
