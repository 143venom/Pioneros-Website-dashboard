from typing import Any
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    logo = models.ImageField(
        upload_to="images/headerlogo/", default=None, null=True, blank=True
    )

    def __str__(self):
        return self.location


class SocialMedia(models.Model):
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(max_length=255, blank=True, null=True)


class Carousel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/carousels/")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ContactBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/Contactsbackground/")


class Department(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(
        upload_to="images/doctors/", default=None, null=True, blank=True
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class HomeContentTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class HomeContent(models.Model):
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ProductBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/productsbackground/")


class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/products/")

    def __str__(self):
        return self.title


class ServicesBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/servicesbackground/")


class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/services/")

    def __str__(self):
        return self.title


class FeaturesBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/featuresbackground/")


class WarehouseAndLogistic(models.Model):
    image = models.ImageField(upload_to="images/warehouseandlogistic/")


class Feature(models.Model):
    title = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    image = models.ImageField(
        upload_to="images/featureimage/", default=None, blank=True, null=True
    )

    def __str__(self):
        return self.title


class Features_Content(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="images/featurecontent/", default='/img/logo.jpg/', blank=True, null=True
    )

    def __str__(self):
        return self.name
    


class Appointment(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    problems = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.doctor.name} - {self.date} - {self.time} - {self.problems}"


class Testimonial(models.Model):
    image = models.ImageField(upload_to="images/testimonial/")
    message = models.TextField(max_length=255)
    patient_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.patient_name


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class About_Content(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class NewsAndEventBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/newsandeventbackground/")


class News_Events(models.Model):
    image = models.ImageField(upload_to="images/newsandevent/")
    # name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(
        default=timezone.now
    )  # Automatically set on creation
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
