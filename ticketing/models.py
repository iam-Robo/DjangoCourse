from django.db import models

class Movie(models.Model):
    '''
    creates a movie model
    '''
    class Meta():
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'
    name = models.CharField('عنوان',max_length=100)
    director = models.CharField('کارگردان',max_length=50)
    year = models.IntegerField('سال تولید')
    length = models.IntegerField('مدت زمان')
    description = models.TextField('درباره فیلم')
    poster = models.ImageField('پوستر', upload_to='movie_poster/')
    def __str__(self):
        return self.name

class Cinema(models.Model):
    '''
    creates Cinema model
    '''
    class Meta():
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'
    cinema_code = models.IntegerField('کد سینما', primary_key=True)
    name = models.CharField('نام سینما', max_length=50)
    city = models.CharField('شهر', max_length=30, default='تهران')
    capacity = models.IntegerField('گنجایش')
    phone = models.CharField('تلفن', max_length=20, blank=True)
    address = models.TextField('آدرس')
    image = models.ImageField('تصویر', upload_to='cinema_images/', null=True , blank=True) #blank gives ability for deleting picture in admin panel
    def __str__(self):
        return self.name
class ShowTime(models.Model):
    '''
    creates show time of movies in cinema
    '''
    class Meta():
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'
    movie = models.ForeignKey('Movie',on_delete=models.PROTECT,verbose_name='فیلم')
    cinema = models.ForeignKey('Cinema',on_delete=models.PROTECT,verbose_name='سینما')
    start_time = models.DateTimeField('زمان اکران')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('تعداد صندلی های فروخته شده')
    free_seats = models.IntegerField('تعداد صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choice = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیط'),
        (TICKETS_SOLD, 'بلیت ها تمام شدند'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )
    status = models.IntegerField(choices=status_choice)

    def reserve_seat(self, seat_count):
        """
        Reserves one or more seats for a customer
        :param seat_count: An integer as the number of seats to be reserved
        """
        assert isinstance(seat_count, int) and seat_count > 0, 'Number of seats should be a positive integer'
        assert self.status == ShowTime.SALE_OPEN, 'Sale is not open'
        assert self.free_seats >= seat_count, 'Not enough free seats'
        self.free_seats -= seat_count
        if self.free_seats == 0:
            self.status = ShowTime.TICKETS_SOLD
        self.save()

    def __str__(self):
        name = str(self.movie),str(self.cinema)
        return str(name) #to show name of movie and cinema in admin panel(adding scence)

class Ticket(models.Model):
    """
       Represents one or more tickets, bought by a user in an order
    """
    class Meta:
        verbose_name = 'بلیط'
        verbose_name_plural = 'بلیط'

    showtime = models.ForeignKey('ShowTime', on_delete=models.PROTECT, verbose_name='سانس')
    customer = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, verbose_name='خریدار')
    seat_count = models.IntegerField('تعداد صندلی')
    order_time = models.DateTimeField('زمان خرید', auto_now_add=True)

    def __str__(self):
        return '{} بلیط یه نام {} در {} صادر شد'.format(self.seat_count, self.customer, self.order_time)
