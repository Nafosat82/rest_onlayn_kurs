from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView
from .serializers import AboutusSerializer
from rest_framework.permissions import  IsAuthenticated,IsAdminUser,AllowAny
from .models import  *

class ListCreateAboutus(ListCreateAPIView):
    queryset = Aboutus.objects.all()
    serializer_class = AboutusSerializer
    permission_classes = [IsAdminUser,]

class AboutusRetrieveAPIView(RetrieveAPIView):
    queryset = Aboutus.objects.all()
    serializer_class = AboutusSerializer
    permission_classes = [AllowAny,]

class AboutusDelete(DestroyAPIView):
    queryset = Aboutus.objects.all()
    serializer_class = AboutusSerializer
    permission_classes = [IsAdminUser,]