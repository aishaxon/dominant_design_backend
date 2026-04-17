from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()

    def __str__(self):
        return self.name


class VideoProject(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    video = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Partner(models.Model):
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return "Partner"


class Pricing(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    features = models.TextField(help_text="Har bir feature yangi qatorda yoziladi")

    def __str__(self):
        return f"{self.name} - {self.price}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name