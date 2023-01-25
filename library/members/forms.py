from django import forms
from .models import Member

class BookTakenForm(forms.ModelForm):
    address = forms.CharField(
        label = 'Your Address',
        widget = forms.Textarea(attrs={
             'rows': 5,
            
        } )
    )
    email = forms.EmailField(
        widget= forms.TextInput(
            attrs= {
                'style': 'text-transform: lowercase'
            }
        ))
    phone_number = forms.CharField(
        label = "Phone Number",
        widget = forms.TextInput(attrs={
            # 'type': 'number',
            'data-mask': '+91 0000000000'
        })
    )
    member_id = forms.CharField(
        label = "Member Id",
        widget = forms.TextInput(attrs={
            # 'type': 'number',
            'style': 'text-transform: uppercase',
            'data-mask': '(AR) 0000 0000',
            
        })
    )
    class Meta:
        model = Member
        # fields = '__all__'
        exclude = ['taken_date', 'return_date']


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Member
        # fields = '__all__'
        exclude = ['taken_date','email', 'address']