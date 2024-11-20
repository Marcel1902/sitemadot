
from django.contrib import admin
from .models import Destination, DayItinerary
from  django.utils.translation import gettext_lazy as _

class DayItineraryInline(admin.TabularInline):
    model = DayItinerary
    extra = 1

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DayItineraryInline]
    list_display = ('pays', 'continent', 'prix')
    search_fields = ('pays', 'continent')
    list_filter = ('continent',)

admin.site.site_title = _("MADOT")
admin.site.site_header = _('MADOT Administration')
admin.site.index_title = _('Welcome to MADOT Administration')
