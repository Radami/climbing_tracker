from django.contrib import admin

from .models import Grade, Climb, Session, SessionPartner, Location

# Register your models here.
admin.site.register(Grade)
admin.site.register(Climb)
admin.site.register(SessionPartner)


class ClimbInline(admin.TabularInline):
    model = Climb
    extra = 3

class SessionPartnerInline(admin.TabularInline):
    model = SessionPartner
    extra = 0

class LocationInLine(admin.TabularInline):
    model = Location
    extra = 0

class LocationAdmin(admin.ModelAdmin):

   list_display = ['name', 'owner']
    # list_display = [field.name for field in Location._meta.get_fields()]

admin.site.register(Location, LocationAdmin)

class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields' : ['date', 'location', 'owner']}),
        ('Session information', {'fields' : ['rating']})
    ]
    inlines = [ClimbInline, SessionPartnerInline]

    list_display = ('date', 'rating', 'location')
    
    list_filter = ['date', 'location']

admin.site.register(Session, SessionAdmin)

