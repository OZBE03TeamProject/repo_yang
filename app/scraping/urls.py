from django.urls import path
from scraping.views import KakaoMapScraper

urlpatterns = [
    path('execute/', KakaoMapScraper().scraping_view, name='scraping_view'),
]
