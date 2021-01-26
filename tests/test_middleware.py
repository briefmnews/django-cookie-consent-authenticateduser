import pytest

from django.http import HttpResponse

from cookie_consent_authenticateduser.middleware import (
    CheckAuthenticatedUserCookieContentMiddleware,
)

pytestmark = pytest.mark.django_db


def dummy_middleware(request):
    response = HttpResponse()
    response.status_code = 200
    return response


class TestCheckAuthenticatedUserCookieContentMiddleware:
    def test_init(self):
        """Testing the __init__ method"""
        # GIVEN / WHEN
        middleware = CheckAuthenticatedUserCookieContentMiddleware("response")

        # THEN
        assert middleware.get_response == "response"

    def test_with_authenticated_user_without_preferences(self, request_builder, user):
        # GIVEN
        request = request_builder.get(user=user)
        middleware = CheckAuthenticatedUserCookieContentMiddleware(dummy_middleware)

        # WHEN
        response = middleware(request)

        # THEN
        assert response.status_code == 200

    def test_with_authenticated_user_with_preferences(
        self, request_builder, user_with_preferences
    ):
        # GIVEN
        request = request_builder.get(user=user_with_preferences)
        middleware = CheckAuthenticatedUserCookieContentMiddleware(dummy_middleware)

        # WHEN
        response = middleware(request)

        # THEN
        assert response.status_code == 200
