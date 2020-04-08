from django.contrib import admin
from .models import User
from .models import Room

admin.site.register(User)
admin.site.register(Room)