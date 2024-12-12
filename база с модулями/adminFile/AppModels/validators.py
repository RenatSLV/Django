from django.core.exceptions import ValidationError

def validate_more_zero(value):
    if value < 0:
        raise ValidationError(f'Значение {value} должно быть положительным числом или нулем.')
