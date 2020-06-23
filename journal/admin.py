from django.contrib import admin

from .models import Grade, Climb, Session

# Register your models here.
admin.site.register(Grade)
admin.site.register(Climb)
admin.site.register(Session)

