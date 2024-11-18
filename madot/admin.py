
from django.contrib import admin
from .models import Destination, DayItinerary

class DayItineraryInline(admin.TabularInline):
    model = DayItinerary
    extra = 1

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DayItineraryInline]
    list_display = ('pays', 'continent', 'prix')
    search_fields = ('pays', 'continent')
    list_filter = ('continent',)
