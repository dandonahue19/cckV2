from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=50)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Listing(models.Model):
    header = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.header

DRIVE=(
    ('AWD', 'AWD'),
    ('RWD', 'RWD'),
    ('FWD', 'FWD'),
    ('4WD', '4WD')
)
FUEL=(
    ('Gas', 'Gas'),
    ('Diesel', 'Diesel'),
    ('Hybrid', 'Hybrid'),
    ('Electric', 'Electric')
)
TITLE = (
    ('Clean', 'Clean'),
    ('Salvage', 'Salvage'),
    ('Rebuilt', 'Rebuilt'),
    ('Parts', 'Parts')
)
TRANS = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual')
)

class Vehicle(Listing):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.IntegerField()
    mileage = models.IntegerField()
    vin = models.CharField(max_length=20)
    drive = models.CharField(max_length=20, choices=DRIVE)
    fuel = models.CharField(max_length=20, choices=FUEL)
    paint = models.CharField(max_length=50)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, choices=TITLE)
    transmission = models.CharField(max_length=20, choices=TRANS)
    cylinders = models.IntegerField()
    
    def __str__(self):
        return self.header

class Image(models.Model):
    location = models.ImageField(upload_to='listing_images')
    header = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.location