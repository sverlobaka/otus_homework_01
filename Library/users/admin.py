from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from users.models import MyUser


class MyUserAdmin(UserAdmin):
    pass


admin.site.register(MyUser, UserAdmin)