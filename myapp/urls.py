from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_posts, name='home'),
    path("about/", views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('new_post/', views.add_new_post, name='add_new_post'),
    path('contact/', views.contact, name='contact')
]