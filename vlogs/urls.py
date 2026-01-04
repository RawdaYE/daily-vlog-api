from django.urls import path
from .views import VlogListCreateView, VlogDetailView

urlpatterns = [
    path('', VlogListCreateView.as_view(), name='vlog-list-create'),
    path('<int:pk>/', VlogDetailView.as_view(), name='vlog-detail'),
]
