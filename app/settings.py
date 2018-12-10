import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n=y_k+e50p3ai&qecpl@ikoxzkf5@9@0b+spuzn^agnm-^=k52'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'api.apps.TodoConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL=True

CORS_ALLOW_METHODS = (
    'GET',
    'PUT',
    'POST',
    'DELETE',
    'OPTIONS',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'origin',
    'user-agent',
    'content-type',
    'accept-encoding',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}