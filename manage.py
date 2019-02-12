#!/usr/bin/env python
import os
import sys
import json

if __name__ == '__main__':
    if os.environ.get("DJANGO_SETTINGS_MODULE", "study.settings.local") == "study.settings.local":
        try:
            with open("./study/settings/properties.json") as properties_file:
                properties = json.loads(properties_file.read())
                for key, value in properties.items():
                    os.environ[key] = value
        except FileNotFoundError as e:
            pass

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)
