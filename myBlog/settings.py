"""
Django settings for myBlog project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h2_&q!t0s2%q7cym=ju9i^u2kv8-_-7!q^%aju^9p@*^j09cmq'

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
    'mdeditor',
    'blog',
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

ROOT_URLCONF = 'myBlog.urls'

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

WSGI_APPLICATION = 'myBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'uploads')
MEDIA_URL = '/media/'

import django_heroku

django_heroku.settings(locals())

import dj_database_url
DATABASES['default']=dj_database_url.config(conn_max_age=600,ssl_require=True)

# MDEDITOR_CONFIGS = {
#     'width': '90%',  # 自定义编辑框宽度
#     'heigth': 500,   # 自定义编辑框高度
#     'toolbar': ["undo", "redo", "|",
#                 "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
#                 "h1", "h2", "h3", "h5", "h6", "|",
#                 "list-ul", "list-ol", "hr", "|",
#                 "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
#                 "emoji", "html-entities", "pagebreak", "goto-line", "|",
#                 "help", "info",
#                 "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
#     'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
#     'image_folder': 'editor',  # 图片保存文件夹名称
#     'theme': 'default',  # 编辑框主题 ，dark / default
#     'preview_theme': 'default',  # 预览区域主题， dark / default
#     'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
#     'toolbar_autofixed': True,  # 工具栏是否吸顶
#     'search_replace': True,  # 是否开启查找替换
#     'emoji': True,  # 是否开启表情功能
#     'tex': True,  # 是否开启 tex 图表功能
#     'flow_chart': True,  # 是否开启流程图功能
#     'sequence': True,  # 是否开启序列图功能
#     'watch': True,  # 实时预览
#     'lineWrapping': False,  # 自动换行
#     'lineNumbers': False  # 行号
# }
