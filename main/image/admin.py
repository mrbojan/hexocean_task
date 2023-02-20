from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Image, Tier, Account
from django.contrib.auth.models import User


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Tier'


class CustomUserAdmin(UserAdmin):
    inlines = (AccountInline, )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image")


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ("name", "thumbnail_size",
                    "generate_expiring_links", "original_links")


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)