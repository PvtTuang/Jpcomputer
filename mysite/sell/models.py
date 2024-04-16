from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

class Cpuseries(models.Model):
    name_series = models.CharField(max_length=100)

    def __str__(self):
        return self.name_series

class Computer(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]
    
    SYSTEM_CHOICES = [
        ('WINDOW', 'WINDOW'),
        ('IOS', 'IOS'),
    ]

    RAM_CHOICES = [
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
    ]

    ROM_CHOICES = [
        ('128', '128'),
        ('256', '256'),
        ('512', '512'),
        ('1TB', '1TB'),
        ('2TB', '2TB'),
        ('3TB', '3TB'),
        ('4TB', '4TB'),
        ('5TB', '5TB'),
    ]

    CPU_BAND_CHOICES = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
    ]

    CPU_GEN_CHOICES = [
        ('CELERON', 'CELERON'),
        ('PENTIUM', 'PENTIUM'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('RYZEN 3', 'RYZEN 3'),
        ('RYZEN 5', 'RYZEN 5'),
        ('RYZEN 7', 'RYZEN 7'),
        ('RYZEN 9', 'RYZEN 9'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image1 = models.ImageField(upload_to='static/product_images/computer/')
    image2 = models.ImageField(upload_to='static/product_images/computer/', blank=True)
    image3 = models.ImageField(upload_to='static/product_images/computer/', blank=True)
    warranty = models.DateTimeField()
    accessorise = models.CharField(max_length=300)
    cpu_band = models.CharField(max_length=50, choices=CPU_BAND_CHOICES)
    cpu_gen = models.CharField(max_length=50, choices=CPU_GEN_CHOICES)
    cpu_series = models.ForeignKey(Cpuseries, on_delete=models.CASCADE)
    ram = models.CharField(max_length=50, choices=RAM_CHOICES)
    rom = models.CharField(max_length=50, choices=ROM_CHOICES)
    gpu = models.CharField(max_length=100)
    system = models.CharField(max_length=50, choices=SYSTEM_CHOICES)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]
    
    SYSTEM_CHOICES = [
        ('WINDOW', 'WINDOW'),
        ('IOS', 'IOS'),
    ]

    RAM_CHOICES = [
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
    ]

    ROM_CHOICES = [
        ('128', '128'),
        ('256', '256'),
        ('512', '512'),
        ('1TB', '1TB'),
        ('2TB', '2TB'),
        ('3TB', '3TB'),
        ('4TB', '4TB'),
        ('5TB', '5TB'),
    ]

    CPU_BAND_CHOICES = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
    ]

    CPU_GEN_CHOICES = [
        ('CELERON', 'CELERON'),
        ('PENTIUM', 'PENTIUM'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('RYZEN 3', 'RYZEN 3'),
        ('RYZEN 5', 'RYZEN 5'),
        ('RYZEN 7', 'RYZEN 7'),
        ('RYZEN 9', 'RYZEN 9'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image1 = models.ImageField(upload_to='static/product_images/notebook/')
    image2 = models.ImageField(upload_to='static/product_images/notebook/', blank=True)
    image3 = models.ImageField(upload_to='static/product_images/notebook/', blank=True)
    warranty = models.DateTimeField()
    accessorise = models.CharField(max_length=300)
    cpu_band = models.CharField(max_length=50, choices=CPU_BAND_CHOICES)
    cpu_gen = models.CharField(max_length=50, choices=CPU_GEN_CHOICES)
    cpu_series = models.ForeignKey(Cpuseries, on_delete=models.CASCADE)
    ram = models.CharField(max_length=50, choices=RAM_CHOICES)
    rom = models.CharField(max_length=50, choices=ROM_CHOICES)
    gpu = models.CharField(max_length=100)
    system = models.CharField(max_length=50, choices=SYSTEM_CHOICES)

    def __str__(self):
        return self.name
    
class Monitor(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('VIEWSONIC', 'VIEWSONIC'),
        ('ZOWIE', 'ZOWIE'),
        ('APPLE', 'APPLE'),
    ]

    SIZE_CHOICES = [
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('21', '21'),
        ('23', '23'),
        ('24', '24'),
        ('27', '27'),
        ('30', '30'),
        ('32', '32'),
        ('34', '34'),
    ]

    PANEL_CHOICES = [
        ('TN', 'TN'),
        ('VA', 'VA'),
        ('IPS', 'IPS'),
        ('OLED', 'OLED'),
        ('QLED', 'QLED'),
    ]

    REFRESH_RATE_CHOICES = [
        ('60Hz', '60Hz'),
        ('75Hz', '75Hz'),
        ('100Hz', '100Hz'),
        ('144Hz', '144Hz'),
        ('240Hz', '240Hz'),
        ('360Hz', '360Hz'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image_path = models.CharField(max_length=100)
    warranty = models.DateTimeField()
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    panel = models.CharField(max_length=50, choices=PANEL_CHOICES)
    refresh_rate = models.CharField(max_length=50, choices=REFRESH_RATE_CHOICES)

    def __str__(self):
        return self.name
    
class MouseKeyboard(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]

    DPI_CHOICES = [
        # Add your DPI choices here
    ]

    CONNECT_CHOICES = [
        # Add your connection choices here
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image_path = models.CharField(max_length=100)
    warranty = models.DateTimeField()
    dpi = models.CharField(max_length=50, choices=DPI_CHOICES)
    connect = models.CharField(max_length=50, choices=CONNECT_CHOICES)

    def __str__(self):
        return self.name

class HeadphoneSpeakers(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]

    CONNECT_CHOICES = [
        # Add your connection choices here
    ]

    SIZE_CHOICES = [
        # Add your size choices here
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image_path = models.CharField(max_length=100)
    warranty = models.DateTimeField()
    connect = models.CharField(max_length=50, choices=CONNECT_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)

    def __str__(self):
        return self.name

class Printers(models.Model):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('ASUS', 'ASUS'),
        ('ACER', 'ACER'),
        ('LENOVO', 'LENOVO'),
        ('MSI', 'MSI'),
        ('APPLE', 'APPLE'),
    ]

    COLOR_CHOICES = [
        # Add your color choices here
    ]

    INK_TYPE_CHOICES = [
        # Add your ink type choices here
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image_path = models.CharField(max_length=100)
    warranty = models.DateTimeField()
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    type_of_ink = models.CharField(max_length=50, choices=INK_TYPE_CHOICES)

    def __str__(self):
        return self.name
    
class SDCards_USBs(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    capacity = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_path = models.CharField(max_length=100)
    warranty = models.DateTimeField()

    def __str__(self):
        return self.name
    
class ConnectivityDevices(models.Model):
    TYPE_CHOICES = [
        ('Type1', 'Type1'),
        ('Type2', 'Type2'),
        ('Type3', 'Type3'),
    ]
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image_path = models.CharField(max_length=100)
    warranty = models.DateTimeField()

    def __str__(self):
        return self.name