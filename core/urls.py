from django.urls import path
from .views import PathfinderView

urlpatterns = [
    path('pathfinder/', PathfinderView.as_view(), name='find-path'),
]
