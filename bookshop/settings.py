
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# 将logs加入环境变量中
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
# 环境变量操作：小luffyapiBASE_DIR与apps文件夹都要添加到环境变量

import sys
sys.path.insert(0,BASE_DIR)

#
# APPS_DIR = os.path.join(BASE_DIR, 'apps')
# sys.path.insert(1, APPS_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q@d=b10k$&b#uof*y%u#7508&bqi@8%ftynm&+yiwmkjukle3@'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #app注册
    'User',
    'Shop',
    'adminuser'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookshop.wsgi.application'
# DATABASE SET

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',       # 数据库引擎
        'NAME': 'book',                             # 创建的数据库用户名
        'USER': 'root',                             # 数据库用户名
        'PASSWORD': '123',                          # 密码
        'HOST': '127.0.0.1',                        # 主机
        'PORT': '3306',                             # 数据库使用的端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国际化
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 静态文件的路径
STATICFILES_DIRS=[
   os.path.join(os.path.dirname(BASE_DIR),'static')
]

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用WARNING
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi

             'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "bookshop.log"),

            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

#
# 配置django缓存 - 采用redis数据库
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/10",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#         }
#     }
# }


# # drf配置
# from rest_framework import settings
# REST_FRAMEWORK = {
#     # 异常配置
#     'EXCEPTION_HANDLER': 'utils.exception.exception_handler',
#     # 频率限制配置
#     'DEFAULT_THROTTLE_RATES': {
#         'user': None,
#         'anon': None,
#         'sms': '1/m',
#     },
# }
