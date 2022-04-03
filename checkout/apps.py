from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    '''
    checkout config with method overiding ready method 
    and imorting signals
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
