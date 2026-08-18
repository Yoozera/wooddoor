from django.urls import path
from .views import AboutUsView

app_name = 'aboutus'
urlpatterns = [
    path('', AboutUsView.as_view(), name='about-us'),
]