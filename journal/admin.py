from django.contrib import admin

from .models import Grade, Climb, Session, SessionPartner, Location

# Register your models here.
admin.site.register(Grade)
admin.site.register(Climb)
admin.site.register(SessionPartner)
admin.site.register(Location)

class ClimbInline(admin.TabularInline):
    model = Climb
    extra = 3

class SessionPartnerInline(admin.TabularInline):
    model = SessionPartner
    extra = 0

class LocationInLine(admin.TabularInline):
    model = Location
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields' : ['date', 'location', 'owner']}),
        ('Session information', {'fields' : ['rating']})
    ]
    inlines = [ClimbInline, SessionPartnerInline]

    list_display = ('date', 'rating', 'location')
    
    list_filter = ['date', 'location']

admin.site.register(Session, SessionAdmin)

