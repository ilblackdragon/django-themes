import logging

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed

from .core import Theme, ThemesManager
from .models import UserTheme
from .utils import monkey_patch_template_loaders

logger = logging.getLogger('themes')

class ThemesMiddleware(object):
    
    themes_manager = ThemesManager()

    def __init__(self):
        themes = getattr(settings, 'THEMES', None)
        if not themes:
            logger.warning("There is no themes specified. Themes middleware will be disabled.")
            raise MiddlewareNotUsen()
        for theme in themes:
            self.themes_manager.add_theme(Theme(**theme))
        default_theme = getattr(settings, 'DEFAULT_THEME', 0)
        self.themes_manager.set_default(default_theme)
        if not getattr(settings, 'THEMES_USE_TEMPLATE_LOADERS', False):
            monkey_patch_template_loaders()

    def process_request(self, request):
        settings.request_handler = request
        request.theme = self.themes_manager.default
        if request.user.is_authenticated():
            try:
                request.theme = self.themes_manager.get_theme(UserTheme.objects.get(user=request.user).theme)
            except UserTheme.DoesNotExist:
                pass
