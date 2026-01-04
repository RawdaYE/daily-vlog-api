from django.urls import path
from .views import like_vlog, unlike_vlog, vlog_likes

urlpatterns = [
    path('vlogs/<int:id>/like/', like_vlog),
    path('vlogs/<int:id>/unlike/', unlike_vlog),
    path('vlogs/<int:id>/likes/', vlog_likes),
]
