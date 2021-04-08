from django.contrib import admin

from .models import AuthenticatedUserCookieConsent


class AuthenticatedUserCookieConsentAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "cookiegroup")
    list_filter = ("cookiegroup",)
    raw_id_fields = ("user",)
    search_fields = ("user__email",)


admin.site.register(AuthenticatedUserCookieConsent, AuthenticatedUserCookieConsentAdmin)
