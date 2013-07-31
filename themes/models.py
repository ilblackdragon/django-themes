# -*- coding: utf-8 -*-
from django.db import models
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext


class UserTheme(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='user_theme')
    theme = models.IntegerField(_("Theme"), default=0)

    def __unicode__(self):
        return _("User %s uses theme #%d") % (unicode(self.user), self.theme)
