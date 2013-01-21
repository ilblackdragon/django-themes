..   -*- mode: rst -*-

django-themes
##############

**Django themes** is django application that brings a flexible, configurable theming system to any Django project.

Main features: 

- Different templates and statis\media for different themes.
- Each user can choose different theme to use
- Overriding templates from default theme
- Support Jinja2

.. contents::

Requirements
-------------

- python >= 2.5
- django >= 1.2
- pip >= 0.8

Optional:

- jinja2
- coffin


Installation
------------

**Django themes** should be installed using pip: ::

    pip install git+git://github.com/ilblackdragon/django-themes.git


Setup
------

- Add 'themes' to INSTALLED_APPS: ::

    INSTALLED_APPS += ( 'themes', )

- Add 'themes.middleware.ThemesMiddleware' to MIDDLEWARE_CLASSES: ::

    MIDDLEWARE_CLASSES += ( 'themes.middleware.ThemesMiddleware', )

- Add 'themes.context_processors.themes' to TEMPLATE_CONTEXT_PROCESSORS: ::

    TEMPLATE_CONTEXT_PROCESSORS += ( 'themes.context_processors.themes', )

- Add themes urls to base urls: ::

    url(r'^themes/', include('themes.urls')),   

- See how to configure themes below.

Note: if you have any troubles with seting up django-themes because of our monkey patching django's `find_template`
and coffin's `env`, you can use alternative method by adding djang-themes to TEMPLATE_LOADERS:

- Add 'themes.loaders.themes.Loader' to TEMPLATE_LOADERS and enable special option: ::

    THEMES_USE_TEMPLATE_LOADERS = True
    TEMPLATE_LOADERS += ('themes.loaders.themes.Loader', )


Setup themes
------------

Here is example themes_settings.py file to configure django-themes: ::

    import os.path
    from themes.core import Theme, ThemesManager
    from django.utils.translation import ugettext_lazy as _

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
                                                                                                                                                                                                                           
    THEMES_MANAGER = ThemesManager()                                                                                                                                                                                       
                                                                                                                                                                                                                           
    THEMES_MANAGER.add_theme(Theme(                                                                                                                                                                                        
            name = _("First Theme"),                                                                                                                                                                                     
            description = _("Theme #1"),                                                                                                                                                                              
            screenshot = "/static/theme1/screenshot.png",
            template_dir = "theme1",
            # If you will use TEMPLATE_LOADERS method described in setup section,
            # than you should specify full path
            #template_dir = os.path.join(PROJECT_ROOT, "templates/theme1"),
            static_url = "/static/theme1/",
    ))

    THEMES_MANAGER.add_theme(Theme(
            name = _("Second Theme"),
            description = _("Theme #2"),
            screenshot = "/static/theme2/screenshot.png",
            template_dir = "theme2",
            # If you will use TEMPLATE_LOADERS method described in setup section,
            # than you should specify full path
            #template_dir = os.path.join(PROJECT_ROOT, "templates/theme2"),
            static_url = "/static/theme2/",
    ))

    THEMES_MANAGER.set_default(0)

Add importing of themes_settings to settings.py::

    try:
        from themes_settings import *
    except ImportError:
        pass

Use themes
------------

As soon as themes are setup - they are already used.

Now all your templates are searched in the templates/default-theme-name folder (for example 'site_base.html' is searched in templates/theme1/site_base.html). This means that you'll need to move all your templates from templates/* to templates/default-theme-name/.

If you want to override one of the templates in an another theme - you just create that file in the other template folder templates/theme2/site_base.html and change it as you want.

Users can change theirs theme from http://<your domain>/themes/change (you can put a link to it in your Account Settings page). To change how themes.change page looks like just put an template themes/change.html.

License
-----------

Copyright (C) 2011-2013 Ilya Polosukhin and Vlad Frolov
This program is licensed under the MIT License (see LICENSE)
 
