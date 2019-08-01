from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from listings import models as Listing
from listings import serializers

class VehicleListingsViewSet(viewsets.ModelViewSet):
    queryset = Listing.Vehicle.objects.all()
    serializer_class = serializers.VehicleListingSerializer

    