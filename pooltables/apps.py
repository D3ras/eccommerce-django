from django.apps import AppConfig

class PooltablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pooltables'

    def ready(self):
        import pooltables.signal
