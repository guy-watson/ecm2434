"""
ASGI config for ecm2434 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

# Aurthor: Kaloyan Gaydarov and Taariq Fadhill
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecm2434.settings")

application = get_asgi_application()
