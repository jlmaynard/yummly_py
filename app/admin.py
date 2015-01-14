#Admin file, basically allows visibility of models on the admin page.
from django.contrib import admin

from app.models import AppUser
from app.models import YummlyDiet
from app.models import YummlyAllergy
from app.models import ActivityLevel
from app.models import Goal
from app.models import Gender

# Register your models here.
admin.site.register(AppUser)
admin.site.register(YummlyDiet)
admin.site.register(YummlyAllergy)
admin.site.register(ActivityLevel)
admin.site.register(Goal)
admin.site.register(Gender)