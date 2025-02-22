import os
import sys

print(f"Current working directory: {os.getcwd()}")
print(f"PYTHONPATH: {sys.path}")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users_project.settings')

application = get_wsgi_application()
