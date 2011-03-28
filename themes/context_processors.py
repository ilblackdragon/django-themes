from django.conf import settings

THEMES_MANAGER = getattr(settings, 'THEMES_MANAGER', None)

def themes(request):
    """
    Returns context variables containing information about theme.
    """
    return {
        'MEDIA_URL': request.theme.media_url,
        'STATIC_URL': settings.STATIC_URL
    }
