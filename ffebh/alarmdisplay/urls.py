from django.urls import path
from .views import HomePageView, UhrView, EinsatzView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePageView, name='home'),
    path('uhr', UhrView.as_view(), name='uhr'),
    path('einsatz', EinsatzView, name='einsatz'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
