from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

if 'coffin' in settings.INSTALLED_APPS:
    from coffin.template.response import TemplateResponse
else:
    from django.template.response import TemplateResponse

from themes.models import UserTheme

THEMES = getattr(settings, 'THEMES', None)

@login_required
def change(request, theme_id=None, template_name="themes/change.html"):
    if theme_id:
        theme, is_new = UserTheme.objects.get_or_create(user=request.user)
        theme.theme = theme_id
        theme.save()
        return redirect('themes_change')
    return TemplateResponse(request, template_name, {'themes': THEMES, 'current_theme_id': request.theme.id})
