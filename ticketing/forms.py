from django import forms
from ticketing.models import Cinema


class ShowTimeSearchForm(forms.Form):
    movie_name = forms.CharField(max_length=100, label='نام فیلم', required=False)
    sale_is_open = forms.BooleanField(label='سانس های قابل خرید', required=False)
    movie_min_length = forms.IntegerField(label='حداقل مدت زمان فیلم', min_value=0,max_value=200, required=False)
    movie_max_length = forms.IntegerField(label='حداکثر مدت زمان فیلم', min_value=0,max_value=200, required=False)

    any_price = '0'
    price_1 = '1'
    price_2 = '2'
    price_3 = '3'
    price_choices = (
        (any_price, 'هر قیمتی'),
        (price_1, 'بین  5000 تا 10000 تومان'),
        (price_2, 'بین 10000 تا 15000 تومان'),
        (price_3, 'بین 15000 تا 25000 تومان')
        )
    price_range = forms.ChoiceField(label='محدوده قیمت',choices=price_choices, required=False)
    cinema = forms.ModelChoiceField(label='سینما',queryset=Cinema.objects.all(), required=False)#queryset for Cinema model to get names of cinemas