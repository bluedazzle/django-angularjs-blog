from NewRaPo.settings.base import *

DEBUG = True

TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newrapo',
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',
    }
}


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=app.myblog, app.blog_lab, app.blog_log',
]


INSTALLED_APPS += ('django_nose',)
