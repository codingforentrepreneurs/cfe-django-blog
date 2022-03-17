#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import pathlib
import sys

import dotenv

BASE_DIR = pathlib.Path(__file__).resolve().parent

def main():
    """Run administrative tasks."""
    
    ENV_PATH= BASE_DIR / '.env'
    if ENV_PATH.exists():
        dotenv.read_dotenv(str(ENV_PATH))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfeblog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
