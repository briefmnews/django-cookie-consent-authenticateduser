from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import AuthenticatedUserCookieConsent
from .serializers import AuthenticatedUserCookieConsentSerializer


class CookieConsentAuthenticatedUserListAPIView(ListAPIView):
    serializer_class = AuthenticatedUserCookieConsentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return AuthenticatedUserCookieConsent.objects.filter(user=user)
