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
    phone = models.CharField(max_length=20,blank=True)
    address = models.TextField()
    def __str__(self):
        return self.name
class ShowTime(models.Model):
    '''
    creates show time of movies in cinema
    '''
    movie = models.ForeignKey('Movie',on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema',on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    price = models.IntegerField()
    salable_seats = models.IntegerField()
    free_seats = models.IntegerField()

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choice = (
        (SALE_NOT_STARTED,'فروش آغاز نشده'),
        (SALE_OPEN,'در حال فروش بلیط'),
        (TICKETS_SOLD,'بلیت ها تمام شدند'),
        (SALE_CLOSED,'فروش بلیت بسته شد'),
        (MOVIE_PLAYED,'فیلم پخش شد'),
        (SHOW_CANCELED,'سانس لغو شد'),
    )
    status = models.IntegerField(choices=status_choice)