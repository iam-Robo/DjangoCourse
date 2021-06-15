from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name = 'پروفایل کاربری'
        verbose_name_plural = 'پروفایل کاربری'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب کاربری')
    # important fields that are stored in User model by Django itself:
    #   first_name, last_name, email, date_joined
    mobile = models.CharField('تلفن همراه', max_length=11)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = ((MALE, 'مرد') , (FEMALE, 'زن'))
    gender = models.IntegerField('جنسیت', choices=GENDER_CHOICE, null=True, blank=True)
    birth_date = models.DateTimeField('تاریخ تولد', null=True, blank=True)
    address = models.TextField('آدرس', null=True, blank=True)
    profile_image = models.ImageField('تصویر', upload_to='users/profile_images/', null=True, blank=True)
    balance = models.IntegerField('میزان اعتبار', default=0)

    def __str__(self):
        return self.user.get_full_name()

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def spend(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            self.save()
            return True
