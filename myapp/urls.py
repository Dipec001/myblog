from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_posts, name='get_all_posts'),
    path("about/", views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('new_post/', views.add_new_post, name='add_new_post'),
    path('contact/', views.contact, name='contact'),
    path('posts/<int:post_id>/', views.show_post, name='show_post'),
    path('posts/edit/<int:post_id>/',views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),

]