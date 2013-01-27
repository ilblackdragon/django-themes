from django.conf import settings

THEMES_MANAGER = getattr(settings, 'THEMES_MANAGER', None)

def themes(request):
    """
    Returns context variables containing information about theme.
    """
    context = {
        'STATIC_URL': settings.STATIC_URL,
        'THEME_STATIC_URL': settings.STATIC_URL
    }
    theme = getattr(request, 'theme', None)
    if theme is not None:
        context['THEME_STATIC_URL'] = request.theme.static_url
    return context
