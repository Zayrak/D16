from django.apps import AppConfig


class AdvertappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advertApp'

    def ready(self):
        import advertApp.signals
