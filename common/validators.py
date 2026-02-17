from django.core.exceptions import ValidationError


def check_if_is_positive(value):
    if value < 0:
        raise ValidationError('Cannot be less than 0')
    return value