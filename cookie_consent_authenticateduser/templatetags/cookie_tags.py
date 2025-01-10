from django import template
from cookie_consent.conf import settings
from cookie_consent.util import (
    get_cookie_dict_from_request,
    get_cookie_groups,
    get_not_accepted_or_declined_cookie_groups,
)
from cookie_consent_authenticateduser.models import AuthenticatedUserCookieConsent

register = template.Library()  # Register the template tag


def _get_cookie_groups_consent_state(cookie_groups):
    accepted_cookie_groups = {}
    for cookie_group, value in cookie_groups.items():
        accepted_cookie_groups[cookie_group] = bool(
            value != settings.COOKIE_CONSENT_DECLINE
        )
    return accepted_cookie_groups


@register.inclusion_tag('cookie_consent/includes/cookie-banner.html', takes_context=True)
def display_cookie_consent(context):
    """
    Template tag to display cookie consent state.
    Renders a sub-template and passes relevant variables to it.
    """
    request = context['request']  # Access the request object from context
    accepted_cookie_groups = {}
    show_cookie_consent = bool(get_not_accepted_or_declined_cookie_groups(request))

    if show_cookie_consent:
        user = request.user
        if user.is_authenticated:
            user_cookie_consents = AuthenticatedUserCookieConsent.objects.filter(
                user=user
            ).select_related("cookiegroup")
            user_cookie_groups = {consent.cookiegroup for consent in user_cookie_consents}
            show_cookie_consent = not (set(user_cookie_groups) == set(get_cookie_groups()))
            cookie_groups_dict = {
                consent.cookiegroup.varname: str(consent.action)
                for consent in user_cookie_consents
            }
            accepted_cookie_groups = _get_cookie_groups_consent_state(cookie_groups_dict)
    else:
        accepted_cookie_groups = _get_cookie_groups_consent_state(
            get_cookie_dict_from_request(request)
        )

    return {
        "show_cookie_consent": show_cookie_consent,
        "request": request,
        **accepted_cookie_groups
    }
