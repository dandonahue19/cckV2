from rest_framework import serializers
from listings import models as Listings

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        Listings.Image
        fields = '__all__'

class VehicleListingSerializer(serializers.ModelSerializer):
    model_name = serializers.StringRelatedField(source='model.name')
    make_name = serializers.StringRelatedField(source='model.make.name')
    primary_images = serializers.SerializerMethodField()
    class Meta:
        model = Listings.Vehicle
        fields = '__all__'
    
    def get_primary_images(self, obj):
       return obj.images.filter(header=True).values_list('location', flat=True)