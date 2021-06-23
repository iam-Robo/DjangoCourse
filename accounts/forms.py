from django import forms
from django.core.exceptions import ValidationError
from accounts.models import Payment
import re

'''
this is a model form , we use model form when we need to interact with database and models 
otherwise we use normal forms
'''

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'transaction_code']


#custom validations for form

    #transaction must be in 'bank-30000-UHB454GRH73BDYU#' format
    def clean_transaction_code(self):
        code = self.cleaned_data.get('transaction_code')
        if not re.fullmatch('bank-\d*-\w*#', str(code)):
            raise ValidationError('قالب رسید تراکنش معتبر نیست')
        else:
            return code

    #amount must be devideable on 1000
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount % 1000 != 0:
            raise ValidationError('مبلغ پرداختی باید مضربی از هزار باشد')
        else:
            return amount

    #the amount and amount in transaction code must be the same
    def clean(self):
        super().clean()
        amount = self.cleaned_data.get('amount')
        code = self.cleaned_data.get('transaction_code')
        code2 = re.findall('bank-(\d*)-\w*#', code)
        if amount != int(code2[0]):
            raise ValidationError('رسید و مبلغ تراکنش هم‌خوانی ندارند')
