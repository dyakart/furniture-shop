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
# Здесь определяем наши приложения (отдельные логические блоки, которые нам необходимы для проекта)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # подключаем полнотекстовый поиск django
    'django.contrib.postgres',

    # приложение для дополнительной отладки django
    'debug_toolbar',

    # статические страницы
    'main',
    # товары
    'goods',
    'users',
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

    # добавляем дополнительный инструмент для отладки
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# файл urls.py, где указаны все url-адреса нашего приложения
ROOT_URLCONF = 'app.urls'

# шаблонизатор для отрисовки html-страниц
# DIRS - где дополнительно искать шаблоны, указываем папку templates в корне
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
# NAME - имя БД
# USER - имя пользователя; HOST - хост, на котором работает БД (IP-адрес); PORT - порт IP-адреса
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'home',
        'USER': 'home',
        'PASSWORD': 'home',
        'HOST': 'localhost',
        'PORT': '5432',
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
LANGUAGE_CODE = 'ru-ru'

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

# какой префикс будет добавлен, при получении медиа-файлов
MEDIA_URL = 'media/'

# где django будет искать медиа-файлы (в папке media)
MEDIA_ROOT = BASE_DIR / 'media'

# где будет работать дополнительный инструмент для отладки
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# автоинкремент (+1) id для каждой новой записи в БД в каждом приложении
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# указываем какую модель использовать вместо auth_user (нашу дополненную модель)
AUTH_USER_MODEL = 'users.USER'

# путь к нашему представлению login (url-адрес), чтобы переопределить страницу "Not Found" у модуля
# login_required на нашу страницу авторизации
LOGIN_URL = '/user/login/'
