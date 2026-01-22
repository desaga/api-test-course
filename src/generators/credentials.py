# src/generators/credentials.py
import logging
import random
import string

logger = logging.getLogger(__name__)

def get_random_password_and_email(domain=None, email_prefix=None):
    logger.debug('-> get_random_password_and_email')

    if not domain:
        domain = 'test.dev'
    if not email_prefix:
        email_prefix = 'test_user'

    random_email_str_length = 10
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random_email_str_length))
    email = email_prefix + '_'+ random_string + '@' + domain

    password_length = 20
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_length))

    result = {'email': email, 'password': password }
    logger.debug('Generated random password and email: {}'.format(result))
    return result



if __name__ == '__main__':
    get_random_password_and_email(domain='test.dev', email_prefix='test')