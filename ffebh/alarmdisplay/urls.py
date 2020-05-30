from django.urls import path
from .views import HomePageView, UhrView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('uhr', UhrView.as_view(), name='uhr'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
