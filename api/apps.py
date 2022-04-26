from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self):
        from .models import Tweet, DisasterTag, Mark
        from .main import cron_tweet
        print("ready")
        # cron_tweet()