

from django import forms
from multiselectfield import MultiSelectFormField
from django.forms.widgets import SelectDateWidget

# Added code from local system to server system.

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label='Enter your Name :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Name'
            }
        )
    )

    email = forms.EmailField(
        label='Enter your email id :',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter your mobile number :',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contact Number'
            }
        )
    )

    COURSES_CHOICES = (
        ('Python','Python'),
        ('Django','Django'),
        ('REST-API','REST API'),
        ('Flask','Flask'),
    )
    course = MultiSelectFormField(
        choices=COURSES_CHOICES,
        label='Select required courses'
    )

    Location_Choices = (
        ('Hyderabad','Hyderabad'),
        ('Bangalore','Bangalore'),
        ('Chennai','Chennai'),
    )
    location = MultiSelectFormField(
        choices=Location_Choices,
        label='Select Your required locations.'
    )

    y = range(1980,2030)
    start_date = forms.DateField(
        widget=SelectDateWidget(years=y),
        label='Enter requires date'
    )

    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(),
        label='Select your gender'
    )
























