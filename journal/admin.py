from django.contrib import admin

from .models import Grade, Climb, Session, SessionPartner

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

class SessionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields' : ['date', 'center', 'owner']}),
        ('Session information', {'fields' : ['rating']})
    ]
    inlines = [ClimbInline, SessionPartnerInline]

    list_display = ('date', 'rating', 'center')
    
    list_filter = ['date', 'center']

admin.site.register(Session, SessionAdmin)

