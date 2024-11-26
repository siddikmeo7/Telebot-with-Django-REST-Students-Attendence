from rest_framework import serializers
from .models import *

class AttendensSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendens
        fields = ['id','reason', 'attended_time', 'missed_time', 'timeout_time', 'come', 'gone', 'created_at', 'is_active', "user"]

class UsersSerializers(serializers.ModelSerializer):
    attendens = AttendensSerializers(many=True, read_only=True) 

    class Meta:
        model = Users
        fields = ['id', 'username', 'f_name', 'l_name', 'age', 'created_at', 'group', 'is_active', 'attendens']

class GroupsSerializers(serializers.ModelSerializer):
    user = UsersSerializers(many=True, read_only=True)  

    class Meta:
        model = Groups
        fields = ['id', 'name_group', 'sbject_name', 'time', 'created_at', 'is_active', 'user']
