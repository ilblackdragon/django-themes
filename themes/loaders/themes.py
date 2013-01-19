"""
Wrapper for loading templates from the filesystem.
"""

from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loaders.filesystem import Loader as FileSystemLoader
from django.utils._os import safe_join

if 'coffin' in settings.INSTALLED_APPS:
    from jinja2.loaders import split_template_path, FileSystemLoader as Jinja2FileSystemLoader

    class Jinja2Loader(Jinja2FileSystemLoader):
        """
        This is the custom template loader for themes.

        XXX: It uses request, that is hackly added to settings instance by theme middleware.
        This code is not prefectly work because it reset caching if users use different themes.
        """

        def __init__(self, encoding='utf-8'):
            self.encoding = encoding

        def get_source(self, environment, template):
            request = getattr(settings, 'request_handler', None)
            if not request:
                raise TemplateNotFound(template)
            self.searchpath = request.theme.template_dir_list
            try:
                contents, filename, file_uptodate = super(Jinja2Loader, self).get_source(environment, template)
            except:
                raise
            theme_name = request.theme.name
            def uptodate():
                if not file_uptodate():
                    return False
                request = getattr(settings, 'request_handler', None)
                if not request:
                    return False
                if request.theme.name != theme_name:
                    return False
                return True
            return contents, filename, uptodate


class Loader(FileSystemLoader):
    
    def get_template_sources(self, template_name, template_dirs=None):
        """
        Returns the absolute paths to "template_name", when appended to each
        directory in "template_dirs". Any paths that don't lie inside one of the
        template dirs are excluded from the result set, for security reasons.
        """
        if not template_dirs:
            request = getattr(settings, 'request_handler', None)
            if request:
                template_dirs = request.theme.template_dir_list
        return super(Loader, self).get_template_sources(template_name, template_dirs)

