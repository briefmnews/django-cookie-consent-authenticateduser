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
COOKIE_CONSENT_COOKIE_DOMAIN = None

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Add template directories if needed
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",  # Necessary to pass `request` in templates
                "django.contrib.auth.context_processors.auth",
            ],
        },
    },
]

ROOT_URLCONF = "tests.urls"