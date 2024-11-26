from django.contrib import admin
from .models import *

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ["name_group","subject_name","time","created_at",]
    list_filter = ["name_group",'subject_name','time',]

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["telegram_id","username","f_name","l_name","age","created_at",]
    list_filter = ['f_name','l_name','age','group',]
    search_fields = ["username",'f_name','l_name','group','telegram_id']

@admin.register(Attendens)
class AttendensAdmin(admin.ModelAdmin):
    list_display = ["user","reason","attended_time","missed_time","timeout_time","come","gone","created_at",]
    list_filter = ["user","come","gone",]
    search_fields = ["user",]
