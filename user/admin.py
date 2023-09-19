from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasicuserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BasicuserAdmin):
    pass
