from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm, Form, CharField, forms

from users.models import User


class UserRegisterForm(ModelForm):
    """Форма регистрации"""

    class Meta:
        model = User
        fields = ("phone", "city", "telegram_id", "email", "password",)


class AuthCodeForm(Form):
    """Форма ввода кода для авторизации"""

    code = CharField(label="Код авторизации")


class UserUpdateForm(UserChangeForm):
    """Форма обновления данных пользователя"""

    def clean_invite_input(self):
        """Проверяем referral_code"""
        referral_code = self.cleaned_data.get("referral_code")
        if self.instance.referral_code:
            raise forms.ValidationError("Вы уже использовали код")
        if not referral_code:
            return referral_code
        if referral_code == self.instance.referral_code:
            raise forms.ValidationError("Вы не можете использовать свой же код!")
        if not User.objects.filter(invite_code=referral_code).exists():
            raise forms.ValidationError("Пригласительный код не найден!")
        return referral_code

    class Meta:
        model = User
        fields = (
            "phone",
            "email",
            "city",
            "referral_code",
        )
