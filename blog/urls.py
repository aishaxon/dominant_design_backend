from django.urls import path
from .views import *

from django.urls import path
from .views import *

urlpatterns = [
    path('xizmatlar/', ServiceList.as_view()),
    path('portfolio/', PortfolioList.as_view()),
    path('portfolio/<int:pk>/', PortfolioDetail.as_view()),
    path('video-loyihalar/', VideoProjectList.as_view()),
    path('video-loyihalar/<int:pk>/', VideoProjectDetail.as_view()),
    path('galereya/', GalleryList.as_view()),
    path('galereya/<int:pk>/', GalleryDetail.as_view()),
    path('hamkorlar/', PartnerList.as_view()),
    path('hamkorlar/<int:pk>/', PartnerDetail.as_view()),
    path('tariflar/', PricingList.as_view()),
    path('tariflar/<int:pk>/', PricingDetail.as_view()),
    path('jamoa/', TeamList.as_view()),
    path('jamoa/<int:pk>/', TeamDetail.as_view()),
    path('murojaat/', ContactCreate.as_view()),
]