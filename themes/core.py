from os.path import exists, join
from django.conf import settings

#DEBUG_THEME = getattr(settings, 'DEBUG_THEME', True)

class Theme(object):
    
    def __init__(self, name, description, screenshot, template_dir, media_url):
        self.name = name
        self.description = description
        self.screenshot = screenshot
        self.template_dir_debug = template_dir
        if exists(template_dir + '_release'):
            self.template_dir_release = template_dir + '_release'
        else:
            self.template_dir_release = template_dir
        self.media_url_debug = media_url
        if exists(media_url[1:-1] + '_release'):
            self.media_url_release = media_url[:-1] + '_release/'
        else:
            self.media_url_release = media_url
        
    @property
    def template_dir(self):
        if settings.DEBUG_THEME:
            return self.template_dir_debug
        else:
            return self.template_dir_release

    @property
    def media_url(self):
        if settings.DEBUG_THEME:
            return self.media_url_debug
        else:
            return self.media_url_release
            
class ThemesManager(object):
    
    Manager = None
    
    def __init__(self):
        ThemesManager.Manager = self
        self.themes = []
        self.default = None
        
    def add_theme(self, theme):
        self.themes.append(theme)
    
    def get_theme(self, index):
        if index < len(self.themes):
            return self.themes[index]
        return self.default
        
    def set_default(self, index):
        if index < len(self.themes):
            self.default = self.themes[index]
