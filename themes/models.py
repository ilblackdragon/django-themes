# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext

class Theme(models.Model):
    user = models.ForeignKey(User, unique=True, related_name="theme")
    theme = models.IntegerField(_('Theme'), default=0)

    def __unicode__(self):
        return _("User %s uses theme #%d") % (unicode(self.user), self.theme)
