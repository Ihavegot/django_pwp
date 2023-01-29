from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginFormLabels(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginFormLabels, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Login"
        self.fields['password'].label = "Hasło"
        self.error_messages['invalid_login'] = "Niepoprawny login lub hasło!"
        self.error_messages['inactive'] = "Takie konto nie istnieje!"
        print(self.error_messages)
