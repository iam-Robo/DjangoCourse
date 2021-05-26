from django.db import models

class Movie(models.Model):
    '''
    creates a movie model
    '''
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.name

class Cinema(models.Model):
    '''
    creates Cinema model
    '''
    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30,default='تهران')
    capacity = models.IntegerField()
    phone = models.CharField(max_length=20,null=True)
    address = models.TextField()
    def __str__(self):
        return self.name