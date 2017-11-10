from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myApp'
    verbose_name = 'App'
    def ready(self):
      import myApp.signals
