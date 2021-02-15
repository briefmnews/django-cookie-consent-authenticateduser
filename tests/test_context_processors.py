import pytest

from cookie_consent_authenticateduser.context_processors import display_cookie_consent

pytestmark = pytest.mark.django_db


class TestDisplayCookieConsent:
    @pytest.mark.usefixtures("cookie_group")
    def test_no_cookies_set_in_request(self, request_builder):
        # GIVEN
        request = request_builder.get()

        # WHEN
        context = display_cookie_consent(request)

        # THEN
        assert context["show_cookie_consent"]

    def test_cookies_set_in_request(self, request_builder, cookie_group, settings):
        # GIVEN
        request = request_builder.get()
        request.COOKIES[settings.COOKIE_CONSENT_NAME] = f"{cookie_group.varname}=dummy"

        # WHEN
        context = display_cookie_consent(request)

        # THEN
        assert not context["show_cookie_consent"]

    def test_no_cookies_in_request_but_in_database(
        self, request_builder, user_with_preferences
    ):
        # GIVEN
        request = request_builder.get(user=user_with_preferences)

        # WHEN
        context = display_cookie_consent(request)

        # THEN
        assert not context["show_cookie_consent"]

    def test_no_cookies_set_in_request_nor_database(self, request_builder, user):
        # GIVEN
        request = request_builder.get(user=user)

        # WHEN
        context = display_cookie_consent(request)

        # THEN
        assert context["show_cookie_consent"]
