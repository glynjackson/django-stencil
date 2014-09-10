import os
import sys

path = '/srv/PROJECT_FOLDER'
if path not in sys.path:
    sys.path.insert(0, '/srv/PROJECT_FOLDER')

os.environ['DJANGO_SETTINGS_MODULE'] = 'PROJECT_FOLDER.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
