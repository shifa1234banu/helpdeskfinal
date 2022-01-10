from django.urls import path,include
# from watchlist_app.api import views
from organization.api.views import CategoryListAV,CategoryAV,OrganizationListAV,OrganizationAV

urlpatterns = [
    path('list/',CategoryListAV.as_view(),name='category-list'),
    path('<int:pk>/',CategoryAV.as_view(),name='category-details'),
    path('organizationlist/',OrganizationListAV.as_view(),name='organization-list'),
    path('<int:pk>/',OrganizationAV.as_view(),name='organization-details'),

    
]
