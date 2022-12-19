from django.contrib import admin
from .models import Character, Attack, Campaign

# Register your models here.

admin.site.register(Character)
admin.site.register(Attack)
admin.site.register(Campaign)