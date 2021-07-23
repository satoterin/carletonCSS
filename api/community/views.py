from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *


class EventListAll(
    generics.GenericAPIView
):  # List all job events, or create a new  event
    serializer_class = EventSerializer

    def get(self, request):
        events = Event.objects
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventById(generics.GenericAPIView):  # List of events by ID
    def get(self, request, id):
        event = Event.objects.filter(id=id)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationListAll(generics.GenericAPIView):  # List all Organizations
    def get(self, request):
        organization = Organization.objects
        serializer = OrganizationSerializer(organization, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationListByTitle(
    generics.GenericAPIView
):  # List of Organizations by Title/Name
    def get(self, request, title):
        event = Organization.objects.filter(title=title)
        serializer = OrganizationSerializer(event, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MembersList(generics.GenericAPIView):  # List all Members
    def get(self, request):
        member = Member.objects
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnnouncementList(generics.GenericAPIView):  # List all Announcements
    def get(self, request):
        announcement = Announcement.objects
        serializer = AnnouncementSerializer(announcement, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsItemList(generics.GenericAPIView):  # List all New Items
    def get(self, request):
        newsitem = NewsItem.objects
        serializer = NewsItemSerializer(newsitem, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
