from django import forms
from django.core import validators
from myApp.models import SignUp, UserPortfolioInfo
from django.forms import ModelForm
from django.contrib.auth.models import User

"""This is a custom validation to check if name starts and ends with A
def custom_valid(value):
    if value.startswith("A") and value.endswith("A"):
        raise forms.ValidationError("This name is ridiculous!")
        """

class BasicForm(forms.Form):
    #name = forms.CharField(validators=[custom_valid]) this is how to use custom validator
    name = forms.CharField()
    email = forms.EmailField()
    vemail = forms.EmailField(label="Re-enter the email")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget= forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    #instead of writing below function, we wrote a line by using validators

    #this is to validate alll form data at once instead of writing cleaned_datafeild
    def clean(self):
        all_cleaned_data = super().clean()
        if all_cleaned_data['email'] != all_cleaned_data['vemail']:
            raise forms.ValidationError("Entered emails don't match!!")


    """This is not commonly usedm we use core validators
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("BOT BOT BOT!!!")
        return botcatcher
        """


class SignupForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ("name", "email")


class UsersForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")

class UserPortfolioInfoForm(forms.ModelForm):
    class Meta():
        model = UserPortfolioInfo
        fields = ("portfolio", "profile_pic")
