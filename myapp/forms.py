from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BlogPost

class SignUpForm(UserCreationForm):
    email = forms.EmailField()  # Use EmailField for email validation

    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')


    def clean_email(self):
        # Check to make sure email is not already in use
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already in use")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data
        




class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    password = forms.CharField(widget=forms.PasswordInput)
    


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'body', 'img_url']