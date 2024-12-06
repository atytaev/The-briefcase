def paypal_client_id(request):
    from django.conf import settings
    return {'PAYPAL_CLIENT_ID': settings.PAYPAL_CLIENT_ID}