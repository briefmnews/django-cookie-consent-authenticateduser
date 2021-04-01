from distutils.core import setup
from setuptools import find_packages


version = "1.0.0"

CLASSIFIERS = [
    "Framework :: Django",
    "Framework :: Django :: 2.1",
    "Framework :: Django :: 2.2",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]

install_requires = ["Django>=2", "django-appconf", "django-cookie-consent"]


def read(f):
    return open(f, "r").read()


setup(
    name="django-cookie-consent-authenticateduser",
    description="Django cookie consent authenticated user plugin",
    version=version,
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
