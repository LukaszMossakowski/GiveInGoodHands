from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm
from give_in_good_hands.models import MyUser


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), label="")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}), label="")

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Imię"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Nazwisko"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email", "required": True})
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasłą nie są identyczne.')
        password_validation.validate_password(self.cleaned_data.get('password'), None)
        if len(cd['password']) < 8:
            raise forms.ValidationError('Hasło powinno zawierać co najmniej 8 znaków.')
        a = 0
        b = 0
        c = 0
        for sign in cd['password']:
            if sign.isupper():
                a = 1
            if sign.islower():
                b = 1
            if sign.isdigit():
                c = 1
        if a == 0 or b == 0 or c == 0:
            raise forms.ValidationError('Hasło powinno zawierać co najmniej jedną wielką literę, jedną małą literę,'
                                        ' co najmniej jedną cyfrę oraz co najmniej jeden znak specjalny.')
        symbols = '!@#$%^&*()<>,.?/:;{}[]"=-_+'
        for i in symbols:
            if i in cd['password']:
                return cd['password2']
            else:
                raise forms.ValidationError('Hasło powinno zawierać co najmniej jedną wielką literę, jedną małą literę,'
                                            ' co najmniej jedną cyfrę oraz co najmniej jeden znak specjalny.')
        return cd['password2']


class EditProfileForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name')
