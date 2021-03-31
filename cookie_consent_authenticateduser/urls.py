from django.urls import path

from .api import CookieConsentAuthenticatedUserListAPIView

urlpatterns = [
    path('', CookieConsentAuthenticatedUserListAPIView.as_view()),
]