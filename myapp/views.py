from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, BlogPost
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_all_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'all_posts':posts})


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.SignUpForm()
    return render(request, 'register.html', {'form': form})
        

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page after login
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_new_post(request):
    """View for adding new post"""
    if request.method == 'POST':
        form = forms.BlogPostForm(request.POST, request.FILES)  # Add request.FILES for image data
        if form.is_valid():
            new_post = form.save(commit=False)  # Create a new BlogPost instance from the form
            # Assuming the author is the logged-in user
            new_post.author = request.user  # Assign the current user as the author
            new_post.save()  # Save the new blog post
            return redirect('get_all_posts')  # Redirect to a page that displays all posts
    else:
        form = forms.BlogPostForm()  # Create a new empty form instance

    return render(request, 'make-post.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        # Handle form submission here if needed
        pass  # Placeholder for handling form data, processing, or sending emails

    return render(request, 'contact.html')