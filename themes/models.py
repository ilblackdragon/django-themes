# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


class UserTheme(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, unique=True, related_name='user_theme')
    theme = models.IntegerField(_("Theme"), default=0)

    def __unicode__(self):
        return _("User %s uses theme #%d") % (unicode(self.user), self.theme)
