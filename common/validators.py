from django.core.exceptions import ValidationError


def check_if_is_positive(value):
    if value < 0:
        raise ValidationError('Cannot be less than 0.')
    return value

def check_if_is_alpha(value):
    if not value.isalpha():
        raise ValidationError('Name can be only letters.')
    return value

def check_if_is_legal_age(value):
    if not value >= 18:
        raise ValidationError('Employees must be at least 18 years old.')
    return value