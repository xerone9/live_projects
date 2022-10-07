from django.contrib import admin
from .models import Teacher
from .models import Room
from .models import TimeSlot
from .models import TimeTable

admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(TimeSlot)
# admin.site.register(TimeTable)

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    ordering = ('date', 'time_slot',)


