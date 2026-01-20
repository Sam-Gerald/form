from django import forms
from.models import Profile

class ProfileForm(form.ModelsForm):
    class Meta:
        model = Profile
        fields = [
            'Profile_picture', 'name', 'emp_id', 'email',
            'designation', 'department', 'reporting_to', 'mobile'
        ]

from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'name', 'email','category', 'appointment_date',
            'appointment_time', 'reason', 'designated_attendee', 'document'
        ]

from django import forms
from .models import Visitor

class RescheduleMeetForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['appointment_date','appointment_time' ]  # Allow only date and time to be updated
        widgets = {
            'appointment_date': forms.DataInput(attrs={'type': 'data', 'class': 'form-control'})
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
        }