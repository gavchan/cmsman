from config.settings.common import *
import yaml

print("Using production settings")

with open(os.path.join(CONFIG_DIR, 'dj_secret.key')) as f:
    SECRET_KEY = f.read().strip()

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [hostname]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Read settings from yaml file
with open(os.path.join(CONFIG_DIR, 'db_settings_prod.yml')) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    default_db = data['default'][0]
    cms_db = data['cms_db'][0]
    hostname = data['allowed_hosts']

print(f'Using CMS MySql database at {cms_db["host"]}:{cms_db["port"]}')

DATABASE_ROUTERS = ['db_routers.cms.CmsDbRouter', ]
DATABASE_APPS_MAPPING = {
    'cmsacc': 'cms_db',
    'cmsinv': 'cms_db',
    'cmssys': 'cms_db',
    'drugdb': 'default',
   }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': default_db['name'],
        'USER': default_db['user'],
        'PASSWORD': default_db['password'],
        'HOST': default_db['host'],
        'PORT': default_db['port'],
    },
    'cms_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': cms_db['name'],
        'USER': cms_db['user'],
        'PASSWORD': cms_db['password'],
        'HOST': cms_db['host'],
        'PORT': cms_db['port'],
    },
}

# Misc security settings
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_HSTS_SECONDS = 86400
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
