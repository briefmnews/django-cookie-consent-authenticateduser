from django.dispatch import receiver
from cookie_consent.signals import accept_cookie, decline_cookie

from cookie_consent_authenticateduser.models import AuthenticatedUserCookieConsent


@receiver(accept_cookie)
@receiver(decline_cookie)
def accept_or_decline_cookie_for_authenticated_user(sender, **kwargs):
    request = kwargs.get("request", None)
    cookie_group = kwargs.get("cookie_group", None)
    action = kwargs.get("action", None)

    if request and cookie_group and action:
        user = request.user
        if user.is_authenticated:
            AuthenticatedUserCookieConsent.objects.update_or_create(
                cookiegroup=cookie_group,
                user=user,
                defaults={"action": action, "version": cookie_group.get_version()},
            )
