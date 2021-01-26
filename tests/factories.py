import factory

from django.contrib.auth import get_user_model

from cookie_consent.models import Cookie, CookieGroup
from cookie_consent_authenticateduser.models import AuthenticatedUserCookieConsent


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: f"john{n}@doe.com")


class CookieGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CookieGroup

    varname = factory.Sequence(lambda n: f"group_{n}")
    name = factory.Sequence(lambda n: f"Group {n}")
    description = factory.Sequence(lambda n: f"bla bla {n}")
    is_required = False
    is_deletable = True
    ordering = factory.Sequence(lambda n: n)


class CookieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cookie

    cookiegroup = factory.SubFactory(CookieGroupFactory)
    name = factory.Sequence(lambda n: f"__{n}")
    description = factory.Sequence(lambda n: f"bla bla {n}")
    path = "/"
    domain = "localhost"


class AuthenticatedUserCookieConsentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AuthenticatedUserCookieConsent

    user = factory.SubFactory(UserFactory)
    cookiegroup = factory.SubFactory(CookieGroupFactory)
    action = 1
    version = factory.Sequence(lambda n: f"version-{n}")
