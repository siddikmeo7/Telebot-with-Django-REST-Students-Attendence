from django.db import models


class Groups(models.Model):
    name_group = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    time = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_group

class Users(models.Model):
    telegram_id = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, unique=True)
    f_name = models.CharField(max_length=150, null=True)
    l_name = models.CharField(max_length=150, null=True)
    age = models.IntegerField(null=True)
    group = models.ManyToManyField(Groups, related_name="user",)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True)
    def __str__(self):
        return self.username

class Attendens(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="attendens")
    reason = models.TextField(null=True)
    attended_time = models.DateTimeField(null=True, blank=True)
    missed_time = models.DateTimeField(null=True, blank=True)
    timeout_time = models.DateTimeField(null=True, blank=True)
    come = models.BooleanField(default=False, null=True)
    gone = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f"{self.user.__str__}"
    
