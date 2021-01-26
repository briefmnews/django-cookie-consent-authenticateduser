SECRET_KEY = "dump-secret-key"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "cookie_consent",
    "cookie_consent_authenticateduser",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

COOKIE_CONSENT_NAME = "cookie_test"
