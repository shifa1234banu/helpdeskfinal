from django.urls import path,include
# from watchlist_app.api import views
from faq.api.views import FaqListAV,FaqAV

urlpatterns = [
    path('faqlist/',FaqListAV.as_view(),name='faq-list'),
    path('<int:pk>/',FaqAV.as_view(),name='faq'),
    

    
]