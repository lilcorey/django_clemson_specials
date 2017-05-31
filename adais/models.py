from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
# Create your models here.
class AdaisUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_address = models.CharField(max_length=200)
	user_year_born = models.IntegerField(default=1900)
	user_school = models.CharField(max_length=50)
	#user_first_name
	#user_last_name
	#user_email
	#user_apps_list
#
#LOOK UP models.OnetoOneField
#
	def __str__(self):
		return '%s profile' % (self.user)
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
      AdaisUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.adaisuser.save()

class Restaurant(models.Model):
  restaurantId = models.IntegerField()
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  website = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  #category = models.CharField(default="")
  def __str__(self):
    return '%s' % (self.name)

class Deal(models.Model):
  restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  day = models.IntegerField()
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=140)
  startTime = models.TimeField()
  endTime = models.TimeField()
  #weekly = models.BooleanField()
  def __unicode__(self):
    return '%s - %s' % (self.restaurantId, self.title)
  def get_fields(self):
    return [(field.name, field.value_to_string(self)) for field in Deal._meta.fields]
  def display_day(self):
    for x in DAYS_OF_WEEK:
      if x[0] == self.day:
        return '%s' % x[1]

class OpenHours(models.Model):
  restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  day = models.IntegerField()
  openTime = models.TimeField()
  closeTime = models.TimeField()

# class AdaisRegisteredApp(models.Model):
# 	app_public_key
# 	app_title