"""
WSGI config for matt_e_commerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/opt/bitnami/apps/django/django_projects/matt-e-commerce-2')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/matt-e-commerce-2/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "matt-e-commerce-2.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()