from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, BlogPost, Comment
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from myapp.tasks import send_normal_email
from django.http import HttpResponse


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
            return redirect('get_all_posts')  # Redirect to a success page after login
        else:
            messages.error(request, "Invalid username or password. Please try again.")

            return render(request, 'login.html')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('get_all_posts')

@login_required
def add_new_post(request):
    """View for adding new post"""

    if not request.user.has_perm('myapp.add_blogpost'):
        # Raise PermissionDenied if the user doesn't have permission
        raise PermissionDenied
    
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Email to notify form submitter
        notify_data = {
            'email_subject': "Thank you for contacting us!",
            'email_body': "We have received your message and will get back to you shortly.",
            'to_email': email,
        }

        send_normal_email.delay(notify_data)

        # Prepare email data
        email_data = {
            'email_subject': f"New Contact Form Submission from {name}",
            'email_body': f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            'to_email': 'dpecchukwu@gmail.com',  # Replace with your email address
        }

        # Send email using send_normal_email function
        send_normal_email.delay(email_data)

        # Add a success message or redirect to a thank you page
        messages.success(request, "Your message has been sent!")

        # For example:
        return render(request, 'contact.html')

    return render(request, 'contact.html')



def show_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    form = forms.CommentForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        if request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.user = request.user
            comment.save()
            return redirect('show_post', post_id=post_id)
        else:
            messages.info(request, "Please log in to leave a comment.")
    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if not request.user.has_perm('myapp.change_blogpost'):
        # Raise PermissionDenied if the user doesn't have permission
        raise PermissionDenied
    
    if request.method == 'POST':
        form = forms.BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show_post', args=[str(post.id)]))
    else:
        form = forms.BlogPostForm(instance=post)  # Populate form with existing post data

    # Determine if it's an edit or a new post
    is_edit = True if post_id else False
    
    return render(request, 'make-post.html', {'form': form, 'is_edit': is_edit})


def delete_post(request, post_id):
    """
    View for deleting a blog post. Requires admin permissions.
    """
    post = get_object_or_404(BlogPost, id=post_id)
    if not request.user.has_perm('myapp.delete_blogpost'):
        raise PermissionDenied
    
    post.delete()
    return HttpResponseRedirect(reverse('get_all_posts'))


def health_check(request):
    # You can customize the response as needed
    return HttpResponse("OK")

