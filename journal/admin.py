from django.contrib import admin

from .models import Grade, Climb, Session

# Register your models here.
admin.site.register(Grade)
# admin.site.register(Climb)

class ClimbInline(admin.TabularInline):
    model = Climb
    extra = 3

class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields' : ['date', 'center']}),
        ('Session information', {'fields' : ['rating']})
    ]
    inlines = [ClimbInline]

    list_display = ('date', 'rating', 'center')
    
    list_filter = ['date', 'center']

admin.site.register(Session, SessionAdmin)

