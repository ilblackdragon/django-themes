from django.conf import settings
from themes.models import Theme

THEMES_MANAGER = getattr(settings, 'THEMES_MANAGER', None)

class ThemesMiddleware(object):
    def process_request(self, request):
        settings.request_handler = request
        request.theme = THEMES_MANAGER.default
        if request.user.is_authenticated():
            try:
                request.theme = THEMES_MANAGER.get_theme(Theme.objects.get(user=request.user).theme)
            except Theme.DoesNotExist:
                pass
                
