from django.urls import path
from .views import index, home, top_sellers

urlpatterns = [
    path('', home, name='home'),
    path('index/', index),
    path('top-sellers/', top_sellers, name='top_sellers')
]
