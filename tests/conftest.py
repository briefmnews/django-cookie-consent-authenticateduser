import pytest

from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

from .factories import (
    UserFactory,
    CookieGroupFactory,
    AuthenticatedUserCookieConsentFactory,
)


@pytest.fixture
def user_with_preferences():
    user = UserFactory()
    cookiegroup_accepted = CookieGroupFactory()
    cookiegroup_declined = CookieGroupFactory()
    AuthenticatedUserCookieConsentFactory(user=user, cookiegroup=cookiegroup_accepted)
    AuthenticatedUserCookieConsentFactory(
        user=user, cookiegroup=cookiegroup_declined, action=-1
    )

    return user


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def request_builder():
    """Create a request object"""
    return RequestBuilder()


class RequestBuilder:
    @staticmethod
    def get(path="/", user=None):
        rf = RequestFactory()
        request = rf.get(path)
        request.user = user or AnonymousUser()

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        return request
