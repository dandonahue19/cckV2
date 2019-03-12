from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=50)

class Model(models.Model):
    name = models.CharField(max_length=50)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

class Listing(models.Model):
    header = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True)
    description = models.TextField()

class Vehicle(Listing):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='vehicles', on_delete=models.CASCADE)
    year = models.IntegerField()
    mileage = models.IntegerField()
    vin = models.CharField(max_length=20)
    drive = models.CharField(choices=('AWD', 'RWD', 'FWD', '4WD'))
    fuel = models.CharField(choices=('Gas', 'Diesel', 'Hybrid', 'Electric'))
    paint = models.CharField(max_length=50)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    title = models.CharField(choices=('Clean', 'Salvage', 'Rebuilt'))
    transmission = models.CharField(choices=('Automatic', 'Manual'))
    cylinders = models.IntegerField()

class Image(models.Model):
    location = models.ImageField(upload_to='/listing_images'),
    header = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
