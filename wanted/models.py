from django.db import models

# Create your models here.

class Criminal_Info(models.Model):
    criminalid = models.AutoField(primary_key=True)
    criminal_name = models.CharField(max_length=100, null=True, blank=True, default="")
    criminal_image = models.ImageField(upload_to='criminal_images/', null=True, blank=True, default="")
    gender = models.CharField(max_length=100, null=True, blank=True, default="")
    police_station = models.CharField(max_length=100, null=True, blank=True, default="")
    crime_no = models.CharField(max_length=100, null=True, blank=True, default="")
    section_of_law = models.CharField(max_length=100, null=True, blank=True, default="")
    wanted_from_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    date_of_birth = models.CharField(max_length=100, null=True, blank=True, default="")
    height = models.CharField(max_length=100, null=True, blank=True, default="")
    build = models.CharField(max_length=100, null=True, blank=True, default="")
    complextion = models.CharField(max_length=100, null=True, blank=True, default="")
    crime_description = models.CharField(max_length=1000, null=True, blank=True, default="")
    address_criminal = models.CharField(max_length=500, null=True, blank=True, default="")

    def __unicode__(self):
        return self.criminalid

    def __str__(self):
    	return str(self.criminalid) 

class user_criminal_info(models.Model):
    name_of_informer = models.CharField(max_length=100, null=True, blank=True, default="")
    name_of_criminal = models.CharField(max_length=100, null=True, blank=True, default="")
    date = models.DateField(auto_now_add=True)
    info = models.TextField(max_length=1000, null=True, blank=True, default="")
    info_image = models.ImageField(upload_to='useraddedcinfo/', null=True, blank=True, default="")

    def __unicode__(self):
        return self.name_of_informer

    def __str__(self):
    	return str(self.name_of_informer)