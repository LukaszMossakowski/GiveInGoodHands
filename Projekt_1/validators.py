from django import forms


class CharacterValidator:
    def validate(self,password, user=None):
        a = 0
        b = 0
        c = 0
        for sign in password:
            if sign.isupper():
                a = 1
            if sign.islower():
                b = 1
            if sign.isdigit():
                c = 1
        if a == 0 or b == 0 or c == 0:
            raise forms.ValidationError('Password should contain at least one uppercase letter, one lowercase letter,'
                                        ' at least one number and at least one special character.')

    def get_help_text(self):
        return 'Password should contain at least one uppercase letter, one lowercase letter,' \
               ' at least one number and at least one special character.'