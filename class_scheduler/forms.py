from django import forms
from django.forms import ModelForm
from .models import Teacher, Room, TimeSlot, TimeTable


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ("name", "subject", "entry_user")
        labels = {
            'name': "",
            'subject': "",
            "entry_user": "",

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms-format', 'placeholder': "Enter Teacher Name Here"}),
            'subject': forms.TextInput(attrs={'class': 'forms-format', 'placeholder': "Enter Subject Name Here"}),
            'entry_user': forms.HiddenInput(attrs={'class': 'forms-format', 'name': "user",}),

        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ("name", "entry_user")
        labels = {
            'name': "",
            "entry_user": "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms-format', 'placeholder': "Enter Room Name Here"}),
            'entry_user': forms.HiddenInput(attrs={'class': 'forms-format', 'name': "user",}),
        }


class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ("time", "entry_user")
        labels = {
            'time': "",
            "entry_user": "",
        }
        widgets = {
            'time': forms.HiddenInput(attrs={'class': 'forms-format', 'placeholder': "Enter New Timeslot Here", 'value': "acid"}),
            'entry_user': forms.HiddenInput(attrs={'class': 'forms-format', 'name': "user",}),
        }


class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = ("date", "teacher_name_subject", "time_slot", "room_name", "entry_user")
        labels = {
            'date': "",
            "teacher_name_subject": "",
            "time_slot": "",
            "room_name": "",
            "entry_user": "",
        }

        widgets = {
            'date': forms.HiddenInput(attrs={'class': 'forms-format', 'placeholder': "Enter Date", 'id': "store_date", 'name': "store_date"}),
            'teacher_name_subject': forms.Select(attrs={'class': 'forms-format',}),
            'time_slot': forms.Select(attrs={'class': 'forms-format', 'placeholder': "Select Time"}),
            'room_name': forms.Select(attrs={'class': 'forms-format', 'placeholder': "Select Room"}),
            'entry_user': forms.HiddenInput(attrs={'class': 'forms-format', 'name': "user",}),
        }