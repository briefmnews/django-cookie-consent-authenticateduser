from cookie_consent.models import ACTION_ACCEPTED
from cookie_consent.conf import settings
from cookie_consent.util import (
    set_cookie_dict_to_response,
    get_not_accepted_or_declined_cookie_groups,
)

from cookie_consent_authenticateduser.models import AuthenticatedUserCookieConsent


class CheckAuthenticatedUserCookieContentMiddleware:
    """
    Set existing cookie consent to the response if no cookies are
    set in the browser and if the user is authenticated
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if bool(get_not_accepted_or_declined_cookie_groups(request)) and request.user:
            if request.user.is_authenticated:
                user_cookie_consents = AuthenticatedUserCookieConsent.objects.filter(
                    user=request.user
                )
                cookie_dic = {}
                for user_cookie_consent in user_cookie_consents:
                    cookie_group = user_cookie_consent.cookiegroup
                    if user_cookie_consent.action == ACTION_ACCEPTED:
                        cookie_dic[cookie_group.varname] = cookie_group.get_version()
                    else:
                        cookie_dic[
                            cookie_group.varname
                        ] = settings.COOKIE_CONSENT_DECLINE

                set_cookie_dict_to_response(response, cookie_dic)

        return response
