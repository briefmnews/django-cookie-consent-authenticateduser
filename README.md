# django-cookie-consent-authenticateduser
[![Python 3](https://img.shields.io/badge/python-3.7|3.8|3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Django 3](https://img.shields.io/badge/django-3.x-blue.svg)](https://docs.djangoproject.com/en/3.2/)
![Python CI](https://github.com/briefmnews/django-cookie-consent-authenticateduser/workflows/Python%20CI/badge.svg)
[![codecov](https://codecov.io/gh/briefmnews/django-cookie-consent-authenticateduser/branch/main/graph/badge.svg?token=SXURKTTL1R)](https://codecov.io/gh/briefmnews/django-cookie-consent-authenticateduser)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Plugin for [django-cookie-consent app](https://github.com/briefmnews/django-cookie-consent) that saves user's cookie preferences in the database.

## Installation
You need to install `django-cookie-consent` first:
```
pip install -e git://github.com/briefmnews/django-cookie-consent@plugin#egg=django-cookie-consent
```

Then, install the `django-cookie-consent-authenticateduser` plugin:
```
pip install -e git://github.com/briefmnews/django-cookie-consent-authenticateduser@main#egg=django-cookie-consent-authenticateduser
```

## Setup
In order to make `django-cookie-consent-authenticateduser` works, you'll need to follow the steps below:

### Settings
First, you need to add the app, the middleware and the context processor to your settings:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'cookie_consent',
    'cookie_consent_authenticateduser',
    ...
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'cookie_consent_authenticateduser.middleware.CheckAuthenticatedUserCookieContentMiddleware',
    ...
)

TEMPLATES = [
    {
        ...,
        "OPTIONS": {
            "context_processors": [
                ...,
                "cookie_consent_authenticateduser.context_processors.display_cookie_consent",
                ...,
            ],
        },
    }
]
```

## Tests
Testing is managed by `pytest`. Required package for testing can be installed with:
```
pip install -r requirements.txt
```

To run testing locally:
```
pytest
```