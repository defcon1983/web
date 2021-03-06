"""
WSGI config for web_developer_pe_2_0 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_developer_pe_2_0.settings.production")

#application = get_wsgi_application()

from dj_static import Cling

application = Cling(get_wsgi_application())
