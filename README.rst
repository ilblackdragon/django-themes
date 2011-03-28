..   -*- mode: rst -*-

django-themes
##############

**Django themes** is django application that brings a flexible, configurable theming system to any Django project.

.. contents::

Requirements
-------------

- python >= 2.5
- django >= 1.2
- pip >= 0.8


Installation
------------

**Django themes** should be installed using pip: ::

    pip install git+git://github.com/ilblackdragon/django-themes.git


Setup
------

- Add 'themes' to INSTALLED_APPS ::

  INSTALLED_APPS += ( 'themes', )

- Add 'themes.middleware.ThemesMiddleware' to MIDDLEWARE_CLASSES ::

  MIDDLEWARE_CLASSES += ( 'themes.middleware.ThemesMiddleware', )

- Add 'themes.context_processors.themes' to TEMPLATE_CONTEXT_PROCESSORS ::

  TEMPLATE_CONTEXT_PROCESSORS += ( 'themes.context_processors.themes', )

- Add themes urls to base urls ::

  url(r'^themes/', include('themes.urls')),   

- See services setup bellow.


Use themes
------------

Will be added later
