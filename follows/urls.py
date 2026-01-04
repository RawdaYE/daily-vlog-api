from django.urls import path
from .views import FollowCreateView, UnfollowDestroyView, FollowersListView, FollowingListView

urlpatterns = [
    path('follow/', FollowCreateView.as_view(), name='follow'),
    path('unfollow/<int:following_id>/', UnfollowDestroyView.as_view(), name='unfollow'),
    path('<int:user_id>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('<int:user_id>/following/', FollowingListView.as_view(), name='following-list'),
]
