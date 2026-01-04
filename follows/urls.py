from django.urls import path
from .views import follow_user, unfollow_user, list_followers, list_following

urlpatterns = [
    path('users/<int:id>/follow/', follow_user, name='follow-user'),
    path('users/<int:id>/unfollow/', unfollow_user, name='unfollow-user'),
    path('users/<int:id>/followers/', list_followers, name='user-followers'),
    path('users/<int:id>/following/', list_following, name='user-following'),
]
