from django.urls import path

from contact.views import ContactRequestView, ContactInquiriesView, DeleteInquiry, AcceptOfferFromInquiry

app_name = 'contact'

urlpatterns = [
    path('companies/<slug:company_slug>/contact/', ContactRequestView.as_view(), name='contact_form'),
    path('inquiries/', ContactInquiriesView.as_view(), name='inquiries'),
    path('inquiries/delete/<int:pk>/', DeleteInquiry.as_view(), name='delete_inquiry'),
    path('inquiries/<int:pk>/accept/', AcceptOfferFromInquiry.as_view(), name='accept_inquiry'),
]