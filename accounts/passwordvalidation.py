from django.core.exceptions import ValidationError


class PracticalPasswordValidator:
    def validate(self, password: str, user=None):
        if len(set(password)) < 6:
            raise ValidationError("Your password must contain at least 6 unique characters.")

    def get_help_text(self):
        return 'Your password must contain at least 6 unique characters.'