from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

from themes.models import UserTheme

THEMES = getattr(settings, 'THEMES', None)

@login_required
def change(request, theme_id=None, template_name="themes/change.html"):
    if theme_id:
        theme, is_new = UserTheme.objects.get_or_create(user=request.user)
        theme.theme = theme_id
        theme.save()
        return redirect('themes_change')
    else:
        try:
            theme_info = UserTheme.objects.get(user=request.user)
            current_theme_id = theme_info.theme
        except Theme.DoesNotExist:
            current_theme_id = THEMES_MANAGER.get_default()
    return direct_to_template(request, template_name, {'themes': THEMES, 'current_theme_id': current_theme_id})

