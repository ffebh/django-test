from django.urls import path
from .views import HomePageView, UhrView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('uhr', UhrView.as_view(), name='uhr'),
]
