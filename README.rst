..   -*- mode: rst -*-

django-themes
##############

**Django themes** is django application that brings a flexible, configurable theming system to any Django project.
Main features: 
    - Different templates and statis\media on different themes.
    - Each user can use own theme
    - Overriding templates from default theme

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

- Add 'themes.loaders.themes.Loader' to TEMPLATE_LOADERS ::

  TEMPLATE_LOADERS += ('themes.loaders.themes.Loader', )

- Add 'themes.middleware.ThemesMiddleware' to MIDDLEWARE_CLASSES ::

  MIDDLEWARE_CLASSES += ( 'themes.middleware.ThemesMiddleware', )

- Add 'themes.context_processors.themes' to TEMPLATE_CONTEXT_PROCESSORS ::

  TEMPLATE_CONTEXT_PROCESSORS += ( 'themes.context_processors.themes', )

- Add themes urls to base urls ::

  url(r'^themes/', include('themes.urls')),   

- See how to configure themes below.


Setup themes
------------

Will be added later

Use themes
------------

Will be added later

License
-----------

Copyright (C) 2011 Ilya Polosukhin
This program is licensed under the MIT License (see LICENSE)
 
