from django.apps import AppConfig

class myAppNameConfig(AppConfig):
    name = 'myAppName'
    verbose_name = 'A Much Better Name'

class PictureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'picture'
