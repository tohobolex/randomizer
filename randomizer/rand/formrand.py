from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

CATEGORY_FOOD = (
    ('all options', 'all options'),
    ('pork', 'pork'),
    ('chicken', 'chicken'),
    ('vegetarian', 'vegetarian')
)
DIFFICULTY_FOOD = (
    ('all options', 'all options'),
    ('easy', 'easy'),
    ('moderate', 'moderate'),
    ('hard', 'hard')
)
CUISINE_FOOD = (
    ('all options', 'all options'),
    ('american', 'american'),
    ('australian', 'australian'),
    ('european', 'european')
)

class RandForm(forms.Form):
    category = forms.ChoiceField(widget=forms.RadioSelect, choices=CATEGORY_FOOD, initial='all options', required=True)
    difficulty = forms.ChoiceField(widget=forms.RadioSelect, choices=DIFFICULTY_FOOD, initial='all options', required=True)
    cuisine = forms.ChoiceField(widget=forms.RadioSelect, choices=CUISINE_FOOD, initial='all options', required=True)


#class CommentForm(forms.ModelForm):         another possibility
 #   class Meta:
 #       model = Comment
 #       fields = ('name', 'email', 'body')
 #        widgets = {
 #            'name':forms.TextInput(attrs={"class":"form-control"})
 #            'email':forms.EmailInput(attrs={"class":"form-control item"})
 #        }

class CommentForm(forms.Form):
    name = forms.CharField(max_length=80, label='Your name:', widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='E-mail:', widget=forms.EmailInput(attrs={"class":"form-control item"}))
    body = forms.CharField(label='Text:', widget=forms.Textarea(attrs={"class":"form-control"}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='E-mail:', widget=forms.EmailInput(attrs={"class":"form-control item"}))
    password1 = forms.CharField(label='Password:', help_text='(your password must be at least 8 characters including a lowercase letter, an uppercase letter, and a number)', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))