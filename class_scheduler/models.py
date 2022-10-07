from django.db import models




# teacher_name = ['Umer', 'Usman', 'Sarah', 'Haider', 'Zaman']
# teacher_subject = ['Graphics Designing', 'Advance Python', 'Financial Management', 'Pro Gaming', 'Medical']

# k = 0
# for x in teacher_subject:
#     b = Teacher(name=name.value, subject=subject.value)
#     b.save()
#     k += 1

class Teacher(models.Model):
    name = models.CharField('name', max_length=120)
    subject = models.CharField('subject', max_length=120)
    entry_user = models.CharField('entry_user', max_length=120, blank=True)

    def __str__(self):
        return self.name + ' - (' + self.subject + ')'


class Room(models.Model):
    name = models.CharField('Room Name', max_length=120)
    entry_user = models.CharField('entry_user', max_length=120, blank=True)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    time = models.CharField('From_to_To', max_length=120, blank=True)
    entry_user = models.CharField('entry_user', max_length=120, blank=True)

    def __str__(self):
        return self.time


class TimeTable(models.Model):
    date = models.DateField('Schedule Date', null=True)
    teacher_name_subject = models.CharField("Teacher", null=True, max_length=120)
    time_slot = models.CharField("TimeSlot", null=True, max_length=120)
    room_name = models.CharField("Room", null=True, max_length=120)
    entry_user = models.CharField('entry_user', max_length=120)

    def __str__(self):
        return str(self.date)
#
