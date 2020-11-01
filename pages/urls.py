# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [




    path('project_ideas/', AboutPageView.as_view(), name='project_ideas'),
    path('', HomePageView.as_view(), name='home'),
]
