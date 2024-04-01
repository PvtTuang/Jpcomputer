from django.db import models

# Create your models here.

class CPUSeries(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Computer(models.Model):
    BRAND = [
        ('Apple','Apple'),
        ('Acer','Acer'),
        ('Asus','Asus'),
        ('Dell','Dell'),
        ('HP','HP'),
        ('Lenovo','Lenovo'),
        ('Microsoft','Microsoft'),
        ('Samsung','Samsung'),
    ]

    ACCESSORIES = [
        ('เมาส์','เมาส์'),
        ('แป้นพิมพ์','แป้นพิมพ์'),
        ('ลำโพง','ลำโพง'),
        ('หูฟัง','หูฟัง'),
        ('ไมโครโฟน','ไมโครโฟน'),
        ('เว็บแคม','เว็บแคม'),
    ]

    CPU = [
        ('Intel','Intel'),
        ('AMD','AMD'),
        ('Apple Silicon','Apple Silicon'),
    ]

    GEN_CPU = [
        ('M1','M1'),
        ('M2','M2'),
        ('M3','M3'),
        ('M3 Pro','M3 Pro'),
        ('M3 Max','M3 Max'),
        ('Pentium','Pentium'),
        ('Celeron','Celeron'),
        ('I3','I3'),
        ('I5','I5'),
        ('I7','I7'),
        ('I9','I9'),
        ('Ryzen 3','Ryzen 3'),
        ('Ryzen 5','Ryzen 5'),
        ('Ryzen 7','Ryzen 7'),
    ]

    RAM = [
        ('4','4'),
        ('8','8'),
        ('16','16'),
        ('32','32'),
        ('64','64'),
        ('128','128'),
    ]

    ROM = [
        ('128GB','128'),
        ('256GB','256'),
        ('512GB','512'),
        ('1TB','1'),
        ('2TB','2'),
        ('3TB','3'),
        ('4TB','4'),
        ('5TB','5'),
        ('6TB','6'),
        ('7TB','7'),
    ]

    SYSTEM = [
        ('Window','Window'),
        ('macOS','macOS'),
    ]

    TYPE_RAM = [
        ('DDR4','DDR4'),
        ('DDR5','DDR5'),
    ]

    TYPE_ROM = [
        ('HHD','HHD'),
        ('SSD','SSD'),
    ]

    brand = models.CharField(max_length=100, choices=BRAND)
    name = models.CharField(max_length=255,blank=False,null=False)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image1 = models.ImageField(upload_to='static/computer_images/')
    image2 = models.ImageField(upload_to='static/computer_images/')
    image3 = models.ImageField(upload_to='static/computer_images/')
    accessories = models.CharField(max_length=100, choices=ACCESSORIES )
    cpu = models.CharField(max_length=100, choices=CPU)
    cpu_gen = models.CharField(max_length=100, choices=GEN_CPU)
    cpu_series = models.ForeignKey(CPUSeries, on_delete=models.CASCADE)
    ram = models.CharField(max_length=100, choices=RAM)
    ram_gen = models.CharField(max_length=100, choices=TYPE_RAM)
    rom = models.CharField(max_length=100, choices=ROM)
    rom_gen = models.CharField(max_length=100, choices=TYPE_ROM)
    gpu = models.CharField(max_length=255,blank=False,null=False)
    system = models.CharField(max_length=100, choices=SYSTEM)
    warranty = models.DateTimeField()
