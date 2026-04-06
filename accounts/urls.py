from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views import AccountRegisterView, AccountDetailView, AccountDeleteView, ProfileEditView, CompanyListView, \
    CompanyDetailView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', AccountDetailView.as_view(), name='details'),
    path('profile/delete/<int:pk>/', AccountDeleteView.as_view(), name='delete'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='edit'),
    path('companies/', CompanyListView.as_view(), name='companies_list'),
    path('companies/<slug:company_slug>', CompanyDetailView.as_view(), name='company_details')
]