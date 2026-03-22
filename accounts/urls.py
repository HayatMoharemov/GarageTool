from django.urls import path

from accounts.views import AccountRegisterView, AccountLoginView, AccountDetailView

app_name = 'account'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('<int:pk>/', AccountDetailView.as_view(), name='details')
]