from django.apps import AppConfig

class TaskSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_signals'

    def ready(self):
        import task_signals.signals
