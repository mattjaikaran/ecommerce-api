import logging
from django.conf import settings
import stripe

logger = logging.getLogger(__name__)
stripe.api_key = settings.STRIPE_API_KEY

# Customers
# https://stripe.com/docs/api/customers/object?lang=python
def create_customer(user):
    full_name = '{user.first_name} {user.last_name}'
    try:
        response = stripe.Customer.create(email=user.email, name=full_name)
        return response
    except stripe.error.InvalidRequestError as e:
        logger.exception(e)
        return {'error_message': str(e)}

def modify_customer(customer_id, new_email):
    try:
        response = stripe.Customer.modify(customer_id, email=new_email)
        return response
    except stripe.error.InvalidRequestError as e:
        logger.exception(e)
        return {'error_message': str(e)}


def get_customer(customer_id):
    try:
        response = stripe.Customer.retrieve(customer_id)
        return response
    except Exception as e:
        logger.exception(e)
        return {'error_message': e}


def delete_customer(customer_id):
    try:
        response = stripe.Customer.delete(customer_id)
        return response
    except Exception as e:
        logger.exception(e)
        return {'error_message': str(e)}

def get_customers_list(limit=100, account_id=None):
    customers = []
    try:
        response = stripe.Customer.list(limit=limit, stripe_account=account_id)
        customers += response.data
        while response['has_more']:
            response = stripe.Customer.list(
                limit=limit, 
                stripe_account=account_id,
                starting_after=response.data[-1:][0]
            )
            customers += response.data

        return customers
    except Exception as e:
        logger.exception(e)
        return {'error_message': str(e)}

# Subscriptions
# def create_subscription()
# def cancel_subscription()
