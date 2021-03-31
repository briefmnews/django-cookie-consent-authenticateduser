from rest_framework import serializers

from .models import AuthenticatedUserCookieConsent


class AuthenticatedUserCookieConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatedUserCookieConsent
        fields = ['action', 'created', 'cookiegroup']
        depth = 1
