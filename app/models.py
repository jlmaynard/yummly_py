#Models are what is mapped to our tables
from django.db import models
from django.contrib.auth.models import User


#This is essentially an enum which describes any dietary restrictions a user might have
class YummlyDiet(models.Model):
    shortDescription = models.CharField(max_length=50, default="DEFAULT")
    searchValue = models.CharField(max_length=250, default="DEFAULT")

    def __unicode__(self):
        return self.shortDescription


#This is an enum that describes what possible allergies a user might have.
class YummlyAllergy(models.Model):
    shortDescription = models.CharField(max_length=50, default="DEFAULT")
    searchValue = models.CharField(max_length=250, default="DEFAULT")

    def __unicode__(self):
        return self.shortDescription


#Enum describing the user's gender
class Gender(models.Model):
    gender = models.CharField(max_length=250)

    def __unicode__(self):
        return self.gender


#Enum describing the user's activity level
class ActivityLevel(models.Model):
    level = models.CharField(max_length=250)

    def __unicode__(self):
        return self.level


#Enum describing the user's weekly goal
class Goal(models.Model):
    goal = models.CharField(max_length=250)

    def __unicode__(self):
        return self.goal


#This app user is the extension of our user model with all of pyum specific data.
#Doing it this way allows us to use Django's built in user management functions
class AppUser(models.Model):
    user = models.OneToOneField(User)
    yummlydiet = models.ForeignKey(YummlyDiet, default=1)
    allergies = models.ManyToManyField(YummlyAllergy, blank=True)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, default=1)
    height = models.IntegerField()
    activity_level = models.ForeignKey(ActivityLevel, default=1)
    goal = models.ForeignKey(Goal, default=5)
    diabetic = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username