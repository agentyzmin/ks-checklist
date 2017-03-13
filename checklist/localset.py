from .settings import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'checklist_db',
        'USER': 'leonidivanov',
        'PASSWORD': '486ak7wy4',
    }
}
