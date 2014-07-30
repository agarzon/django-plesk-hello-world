#!/usr/bin/env python
import os
import sys

# Add a custom path. Must replace domain.com !!! 
sys.path.append("/var/www/vhosts/domain.com/httpdocs/");

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
