import datetime

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith("vk.team") or email.endswith("corp.mail.ru")):
            raise forms.ValidationError("Ну ты квадробобер конечно, используй корпоративную почту!")
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', "Male"), ('F', "Female")])


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(initial=datetime.date.today(), widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                             'type': "date"}))
    gender = forms.ChoiceField(choices=[('M', "Male"), ('F', "Female")], widget=forms.RadioSelect(attrs={
        'class': "form-check-input"}))
    message = forms.ChoiceField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()