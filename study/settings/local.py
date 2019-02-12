#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from .base import *

##################################################################
# Application configuration
##################################################################
SETTINGS_PATH = os.path.dirname(os.path.abspath(__file__))
PROPERTIES_FILE = os.path.join(SETTINGS_PATH, 'properties.json')

try:
    with open(PROPERTIES_FILE) as properties_file:
        properties = json.loads(properties_file.read())
        for key, value in properties.items():
            os.environ[key] = value
except FileNotFoundError as e:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['STUDY_SECRET'],

DEBUG = os.environ.get("IS_DEBUG", "False").upper() == "TRUE"

ALLOWED_HOSTS = ['*']

##################################################################
# Study App Local configuration
##################################################################


##################################################################
# AWS settings
##################################################################


##################################################################
# Static and Media settings
##################################################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (

)

# The list of finder backends that know how to find static files
# in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

##################################################################
# Databases settings
##################################################################
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

##################################################################
# Set HTTP Headers Settings
##################################################################
CORS_ORIGIN_ALLOW_ALL = True
