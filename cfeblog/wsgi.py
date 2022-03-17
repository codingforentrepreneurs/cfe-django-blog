"""
WSGI config for cfeblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib

import dotenv
from django.core.wsgi import get_wsgi_application

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / '.env'

if ENV_PATH.exists():
    """
    Load in the .env file 
    If it exists
    """
    dotenv.read_dotenv(str(ENV_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfeblog.settings')

application = get_wsgi_application()
