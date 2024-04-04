"""
Django's settings for app project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = C:\Users\dyako\PycharmProjects\Sites\FurnitureShop\app_main
# базовый путь к проекту (в котором лежит manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@rzjidptfyf!#p()(m44jwwt)kmh%8&@*aqi#q!&f#trdilbbg'

# SECURITY WARNING: don't run with debug turned on in production!
# Меняется на False, когда выкатывается на основной сервер
# (чтобы пользователю не отображалась отладочная информация на странице)
DEBUG = True

# * - указывает, что приложение может работать на любых хостах
# или можно указать свои, например, mysite.com
ALLOWED_HOSTS = ['*']


# Application definition
# Здесь определяем наши приложения (отдельные логические блоки, которые нам необходимы для приложения)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
    # товары
    'goods',
]

# Промежуточное ПО, которое отвечает за безопасность, сессии (автоматическую обработку cookies-файлов на ПК юзеров)...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# файл urls.py, где указаны все url-адреса нашего приложения
ROOT_URLCONF = 'app.urls'

# шаблонизатор для отрисовки html-страниц
# DIRS - где дополнительно искать шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# какой протокол работы используем (wsgi or asgi)
WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# подключение БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# валидаторы паролей (минимальная длина, верхний и нижний регистр и тд)
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# на каком языке работает приложение django, на каком языке будет отображаться admin-панель,
# оповещения для пользователей и тд
LANGUAGE_CODE = 'en-us'

# в какой временной полосе работает приложение
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# какой префикс будет добавлен, при получении статических файлов (css, js и тд), в браузере будет отображаться
# следующий примерный путь: /static/deps/css/style.css
STATIC_URL = 'static/'

# указываем дополнительные места, где django нужно искать статику
# бросаем папку static в корень проекта, так как будем использовать одинаковые зависимости для всех приложений
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# автоинкремент (+1) id для каждой новой записи в БД
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'