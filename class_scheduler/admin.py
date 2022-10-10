from django.contrib import admin
from .models import Teacher, UploadFile
from .models import Room
from .models import TimeSlot
from .models import TimeTable
from .models import TemporaryHoldTimeTable
from .models import FinalHoldTimeTable

admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(UploadFile)
admin.site.register(TemporaryHoldTimeTable)
admin.site.register(FinalHoldTimeTable)

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    ordering = ('date', 'time_slot',)


