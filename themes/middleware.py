from django.conf import settings

from .models import Theme
from .utils import monkey_patch_template_loaders

THEMES_MANAGER = getattr(settings, 'THEMES_MANAGER', None)

class ThemesMiddleware(object):
    
    def __init__(self):
        if not getattr(settings, 'THEMES_USE_TEMPLATE_LOADERS', False):
            monkey_patch_template_loaders()

    def process_request(self, request):
        settings.request_handler = request
        request.theme = THEMES_MANAGER.default
        if request.user.is_authenticated():
            try:
                request.theme = THEMES_MANAGER.get_theme(Theme.objects.get(user=request.user).theme)
            except Theme.DoesNotExist:
                pass
                
