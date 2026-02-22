from django.urls import path

from calculator.views import create_offer, offer

app_name = 'calculator'

urlpatterns = [
    path('', create_offer, name='create_offer'),
    path('offer/<int:pk>', offer, name='offer')
]