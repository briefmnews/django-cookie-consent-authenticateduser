from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cookie_consent.models import ACTION_CHOICES, CookieGroup


class AuthenticatedUserCookieConsent(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    action = models.IntegerField(_("Action"), choices=ACTION_CHOICES)
    cookiegroup = models.ForeignKey(
        CookieGroup,
        verbose_name=CookieGroup._meta.verbose_name,
        on_delete=models.CASCADE,
    )
    version = models.CharField(_("Version"), max_length=32)
    created = models.DateTimeField(_("Created"), auto_now_add=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.cookiegroup.name, self.version)

    class Meta:
        verbose_name = _("User cookie consent")
        verbose_name_plural = _("User cookie consents")
        ordering = ["-created"]
        unique_together = ["user", "cookiegroup"]
