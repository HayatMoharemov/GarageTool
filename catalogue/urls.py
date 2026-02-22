from django.urls import path

from catalogue.views import PartsList, PartsDetails, ServicesList, ServicesDetails, CatalogueLanding

app_name = 'catalogue'

urlpatterns = [
    path('', CatalogueLanding.as_view(), name='catalogue_initial_page'),
    path('services_list', ServicesList.as_view(), name='services_list'),
    path('parts_list', PartsList.as_view(),name='parts_list'),
    path('details/parts/<slug:parts_slug>', PartsDetails.as_view(), name='parts_details'),
    path('details/services/<slug:services_slug>', ServicesDetails.as_view(),name='services_details'),
]