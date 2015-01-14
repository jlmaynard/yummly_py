#The forms are what we will be displaying to the user in the HTML
from django import forms
from django.contrib.auth.models import User

from app.models import AppUser


#User form, maps to user model
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


#User form number two, this is without a login field. Used on the profile page
class UserFormWithoutLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')


#App user form. Maps from App user model. Contains all of pyum specific data.
class AppUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppUserForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = "Height (inches)"
        self.fields['yummlydiet'].label = "Dietary Restriction"
        self.fields['goal'].label = "Goal (lbs per week)"

    class Meta:
        model = AppUser
        fields = ('yummlydiet', 'allergies', 'age', 'gender', 'height', 'diabetic', 'activity_level', 'goal')


#This is the form for recipe search. Does not directly tie to any model.
class RecipeSearchForm(forms.Form):
    ignore_user_preferences = forms.BooleanField()
    current_weight = forms.IntegerField()
    calories_consumed = forms.IntegerField()
    num_meals = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    in_ingredients = forms.CharField()
    ex_ingredients = forms.CharField()
    prep_time = forms.IntegerField()
