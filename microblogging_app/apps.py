from django.apps import AppConfig


class MicrobloggingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microblogging_app'

def ready(self):
    import microblogging_app.signals   