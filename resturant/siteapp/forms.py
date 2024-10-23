from django import forms
from .models import Contact,Reservation
from datetime import time
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email_add', 'phone', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name','id':'contact-name'}),
            'email_add': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email','patterns':'[^ @]*@[^ @]*','id':'contact-email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123-456-7890','pattern':'[0-9]{11}','id':'contact-phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message','rows':'5','id':'contact-message'}),
        }

class ReservationForm(forms.ModelForm):
    TIME_CHOICES = [(time(hour, minute).strftime('%H:%M'), time(hour, minute).strftime('%I:%M %p')) 
                    for hour in range(12, 21) for minute in (0,)]
    
    class Meta:
        model = Reservation
        fields = ['name', 'email_add', 'phone',  'no_of_persons','date_reserved','time_reserved','special_requests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name','id':'name'}),
            'email_add': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com','patterns':'[^ @]*@[^ @]*','id':'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123-456-7890','pattern':'[0-9]{11}','id':'phone'}),
            'no_of_persons': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max:12 persons','id':'people'}),
            'date_reserved': forms.DateInput(attrs={'class': 'form-control','id':'date','type':'date'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Requests','rows':'5','id':'contact-message'}),
        }
    time_reserved = forms.ChoiceField(choices=TIME_CHOICES, label="Select Time", widget=forms.Select(attrs={'class': 'form-control', 'id': 'time'}))