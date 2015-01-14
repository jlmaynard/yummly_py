import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
# This will be totally secret, being a public github repo....
SECRET_KEY = 'iq$-8#slq=%nf#r(bas&o$miin+b_(dxy^wfu(uwe-^y28(wh#'

# SECURITY WARNING: don't run with debug turned on in production!
# ^ Don't tell me what to do.
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#Here is where we say exactly what apps we're running
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'app',
    'django_tables2'
)

# I'm not sure what this does, therefore Django magic
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

# More django magic
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request'
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#Where are the URL's found? Right here.
ROOT_URLCONF = 'pyum.urls'

#Django magic telling the server where the WSGI application lies maybe?
WSGI_APPLICATION = 'pyum.wsgi.application'

#Yes, I realize this is an admin account to postgresql and I'm giving the password out to the public.
#It's a school project, not enterprise level development.
#besides, it's on a micro AWS instance. Go ahead and hack into it, if that makes you think you're cool.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'test',
        'HOST': '54.85.78.54'
    }
}

#We speak english here, localization is for chumps
LANGUAGE_CODE = 'en-us'

#East coast
TIME_ZONE = 'EST'

#Sure use this
USE_I18N = True

#And this
USE_L10N = True

#And that? Oh man, you're crazy.
USE_TZ = True

#Showing where all the static files are buried
STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
STATIC_URL = '/static/'

#Showing where any media files would be if we had any
ABSOLUTE_PATH = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
MEDIA_ROOT = ABSOLUTE_PATH('media/')
