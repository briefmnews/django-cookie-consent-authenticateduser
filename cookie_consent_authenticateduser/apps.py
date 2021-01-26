from django.apps import AppConfig


class CookieConsentAuthenticatedUserConf(AppConfig):
    name = "cookie_consent_authenticateduser"

    def ready(self):
        import cookie_consent_authenticateduser.handlers  # noqa
