from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import datetime
import re

UserModel = get_user_model()

def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('choose another email')
    
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    
    if not username:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('an email is needed')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True

def card_verification(card_number, expiration_date, cvv):
    if not card_number or not expiration_date or not cvv:
        return False

    if not card_number.isdigit() or len(card_number) != 16:
        return False

    if not re.match(r'\d{2}/\d{2}', expiration_date):
        return False

    expiration_month, expiration_year = map(int, expiration_date.split('/'))
    current_date = datetime.datetime.today()
    if current_date.year > 2000 + expiration_year or (current_date.year == 2000 + expiration_year and current_date.month > expiration_month):
        return False

    if not cvv.isdigit() or len(cvv) != 3:
        return False

    return True