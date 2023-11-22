from django.contrib import admin
from .models import Game, OldResult, Reminder
# Register your models here.

admin.site.register(Game)
admin.site.register(OldResult)
admin.site.register(Reminder)