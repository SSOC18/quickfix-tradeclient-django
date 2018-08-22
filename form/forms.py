from django import forms

ACTION_CHOICES = (
    ('1', 'Enter New Order'),
    ('2', 'Cancel Order'),
    ('3', 'Request Market Data'),
    ('4', 'Quit'),
)

VERSION_CHOICES = (
    ('1', 'FIX4.0'),
    ('2', 'FIX4.1'),
    ('3', 'FIX4.2'),
    ('4', 'FIX4.3'),
    ('5', 'FIX4.4'),
    ('6', 'FIX1.1'),
)

SIDE_CHOICES = (
    ('1', 'Buy'),
    ('2', 'Sell'),
    ('3', 'Sell Short'),
    ('4', 'Sell Short Exempt'),
    ('5', 'Cross'),
    ('6', 'Cross Short'),
    ('7', 'Cross Short Exempt'),
)

ORDTYPE_CHOICES = (
    ('1', 'Market'),
    ('2', 'Limit'),
    ('3', 'Stop'),
    ('4', 'Stop Limit'),
)

TIMEINFORCE_CHOICES = (
    ('1', 'Day'),
    ('2', 'IOC'),
    ('3', 'OPG'),
    ('4', 'GTC'),
    ('5', 'GTX'),
)

class HomeForm(forms.Form):
    action = forms.CharField(widget=forms.Select(choices=ACTION_CHOICES), max_length=1)
    version = forms.CharField(widget=forms.Select(choices=VERSION_CHOICES), max_length=1)
    clordid = forms.CharField(label='ClordID', max_length=100)
    price = forms.CharField(label='Price', max_length=100)
    symbol = forms.CharField(label='Symbol', max_length=100)
    ordqty = forms.CharField(label='OrdQty', max_length=100)
    side = forms.CharField(widget=forms.Select(choices=SIDE_CHOICES), max_length=1)
    ordtype = forms.CharField(widget=forms.Select(choices=ORDTYPE_CHOICES), max_length=1)
    timeinforce = forms.CharField(widget=forms.Select(choices=TIMEINFORCE_CHOICES), max_length=1)
    senderid = forms.CharField(label='SenderCompID', max_length=100)
    targetid = forms.CharField(label='TargetCompID', max_length=100)
    targetsubid = forms.CharField(label='TargetSubID', max_length=100)