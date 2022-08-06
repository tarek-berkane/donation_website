from core.settings.base import *

SECRET_KEY = "django-insecure-!uw4zzk$ski-i&-(ih+^li%1tt_qbcocp3+o#o_n+#44jqu6$2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
        "django_browser_reload",
]

MIDDLEWARE +=[
        "django_browser_reload.middleware.BrowserReloadMiddleware",
]

