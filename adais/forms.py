from django import forms
from django.forms import MultiWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from nocaptcha_recaptcha.fields import NoReCaptchaField

from .models import AdaisUser, Deal

DAYS_OF_WEEK = (
    (7, 'All Week'),
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
)

class UserCreateForm(UserCreationForm):
	captcha = NoReCaptchaField()


class addDealForm(forms.ModelForm):
  description = forms.CharField(widget=forms.Textarea, max_length=140)
  daysList = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=DAYS_OF_WEEK)
  startTime = forms.TimeField(required=False)
  endTime = forms.TimeField(required=False)

  class Meta:
    model = Deal
    fields = ['restaurantId', 'title', 'description', 'daysList', 'startTime', 'endTime']


    # day = forms.MultipleChoiceField(
    #   required=True,
    #   widget=forms.CheckboxSelectMultiple,
    #   choices=DAYS_OF_WEEK,
    # )
    #exclude = ['restaurantId']
    #restaurantId = forms.IntegerField(widget=forms.HiddenInput(), initial=123)

  # title = forms.CharField(max_length=50)
  # description = forms.CharField(widget=forms.Textarea, max_length=140)
  # startTime = forms.TimeField(widget=forms.DateTimeInput(format='%H:%M'))
  # endTime = forms.TimeField(widget=forms.DateTimeInput(format='%H:%M'))