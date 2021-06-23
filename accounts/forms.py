from django import forms
from accounts.models import Payment

'''
this is a model form , we use model form wheen we need to interact with database and models 
otherwise we use normal forms
'''

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'transaction_code']