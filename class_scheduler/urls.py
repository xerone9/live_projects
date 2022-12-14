from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_teachers', views.all_teachers, name='view_teachers'),
    path('view_rooms', views.all_rooms, name='view_rooms'),
    path('view_timeslots', views.all_timeslots, name='view_timeslots'),
    path('add_teachers', views.add_teachers, name='add_teachers'),
    path('add_rooms', views.add_rooms, name='add_rooms'),
    path('add_timeslots', views.add_timeslots, name='add_timeslots'),
    path('generate_schedule', views.generate_schedule, name='generate_schedule'),
    path('view_schedule', views.view_schedule, name='view_schedule'),
    path('show_schedule/<schedule_date>', views.show_schedule, name='show_schedule'),
    path('pdf_report/<schedule_date>', views.print_pdf_report, name='pdf_report'),
    path('excel_download/<schedule_date>', views.download_excel_report, name='excel_download'),
    path('select_date_to_generate', views.selet_date_to_generate, name='select_date_to_generate'),
    path('delete_entry/<entry_id>', views.delete_entry, name='delete_entry'),
    path('delete_schedule', views.delete_schedule_list, name='delete_schedule_list'),
    path('delete_schedule/<schedule_date>', views.delete_schedule, name='delete_schedule'),
    path('modify_teacher', views.modify_teacher_list, name='modify_teacher_list'),
    path('modify_teacher/<teacher_id>', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<teacher_id>', views.delete_teacher, name='delete_teacher'),
    path('modify_room', views.modify_room_list, name='modify_room_list'),
    path('modify_room/<room_id>', views.edit_room, name='edit_room'),
    path('delete_room/<room_id>', views.delete_room, name='delete_room'),
    path('modify_timeslot', views.modify_timeslot_list, name='modify_timeslot_list'),
    path('modify_timeslot/<time_id>', views.edit_timeslot, name='edit_timeslot'),
    path('delete_timeslot/<time_id>', views.delete_timeslot, name='delete_timeslot'),
    # Below URLs are under development
    path('time_table_fixer', views.time_table_fixer, name='time_table_fixer'),
    path('generate_fix_schedule', views.generate_fix_schedule, name='generate_fix_schedule'),
]
