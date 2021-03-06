"""
WSGI config for student_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
application = WhiteNoise(application, root="/Users/hkd27/Desktop/testing_8thSem-1/static")
application.add_files("/Users/hkd27/Desktop/testing_8thSem-1/static")