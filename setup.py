import cookie_consent_authenticateduser

from setuptools import setup
from setuptools import find_packages


CLASSIFIERS = [
    "Framework :: Django",
    "Framework :: Django :: 5.2",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

install_requires = ["Django>=3", "django-appconf", "django-cookie-consent"]


def read(f):
    return open(f, "r").read()


setup(
    name="django-cookie-consent-authenticateduser",
    description="Django cookie consent authenticated user plugin",
    version=cookie_consent_authenticateduser.__version__,
    author="Brief.me",
    author_email="tech@brief.me",
    url="https://github.com/briefmnews/django-cookie-consent-authenticateduser",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
