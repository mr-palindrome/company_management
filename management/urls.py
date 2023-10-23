from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from management.views import *
from django.contrib import admin
admin.autodiscover()

app_name = 'TeamManagement'

urlpatterns = [
    path('companies/', CompanyViewNoPK.as_view(), name="company_view_no_pk"),
    path('company/', CreateCompanyCreateCompany.as_view(), name="create_company"),
    path('company/<str:pk>/', CompanyView.as_view(), name="company_view"),
    path('delete-company/<str:pk>/', DeleteCompanyById.as_view(), name="delete_company"),

    path('login/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify-token/', TokenVerifyView.as_view(),name='token_verify'),
]