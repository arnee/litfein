from .base import *
import dj_database_url
import urlparse


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


DATABASES['default'] =  dj_database_url.config()
DATABASES['default'].update({
        'ENGINE': 'dbpool.db.backends.postgresql_psycopg2',
        'OPTIONS': {'MAX_CONNS': 6},
})

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2',
}


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL_PREFIX = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'

redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': '%s:%s:%s' % (redis_url.hostname, redis_url.port, 0),
            'OPTIONS': {
                'PASSWORD': redis_url.password,
        }
    }
}
