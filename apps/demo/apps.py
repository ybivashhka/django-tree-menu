"""
Конфигурация приложения demo
"""
from django.apps import AppConfig


class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.demo'
    verbose_name = 'Демо-страницы' 