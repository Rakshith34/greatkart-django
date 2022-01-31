from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src"{}" width = "30" style = "border-radius:50%;">'.format(object.profile_picture.url))

    thumbnail.short_description = 'Profile Picture'
    list_display = ('user','thumbnail',  'city', 'state', 'country')


admin.site.register(Account)
admin.site.register(UserProfile,UserProfileAdmin)
