import logging
import os
from django.conf import settings
import stripe

logger = logging.getLogger(__name__)
stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = os.environ.get('STRIPE_WEBHOOK_SECRET_KEY')


def stripe_webhook(request):
    event = None
    # Stripe request.body needs decoding
    payload = request.body.decode('utf-8')
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        logger.exception(e)
        raise Exception(e)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.exception(e)
        raise Exception(e)

    # Handle event
    if event['type'] == 'account.updated':
        account = event['data']['object']
        return account
    else:
        raise Exception('Unhandled event type {}'.format(event['type']))