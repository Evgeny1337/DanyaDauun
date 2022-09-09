"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя',min_length=2,max_length=100)
    city = forms.CharField(label='Ваш род занятий',min_length=2,max_length=100)
    role = forms.CharField(label='О каком автомобиле вы мечтаете?',min_length=2,max_length=400)
    computer = forms.ChoiceField(label='Какой сегмент производства авто вам больше нравится?',
                                 choices=(('1','Немецкий'),
                                          ('2','Японский')),initial=1)
    adverst = forms.ChoiceField(label='Какой автомобиль вам больше подходит?',
                                choices=[('1','Легковой'),('2','Джип')], widget=forms.RadioSelect,initial=1)
    notice = forms.BooleanField(label='Хотите получать свежие новости из мира автомобилей на ваш email?',required = False)
    email = forms.EmailField(label='Ваш e-mail',min_length=7)
    message = forms.CharField(label='Опишите машину вашей мечты (не обязательно существующую)',widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':'Комментарий'}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title','description','content','image',}
        labels = {'title':"Заголовок",'description': "Краткое содержание",'content':"Полное содержание",'image':"Картинка"}
    
