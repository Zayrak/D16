from django.urls import path
from .views import *

urlpatterns = [
    path('', AdvertList.as_view()),
    path('<int:pk>', AdvertView.as_view()),
    path('add', AdvertCreateView.as_view()),
    path('edit/<int:pk>', AdvertUpdateView.as_view()),
    path('responses', ResponseList.as_view()),
    path('responses/accept/<int:pk>', ResponseAcceptView.as_view()),
    path('responses/delete/<int:pk>', ResponseDeleteView.as_view()),
]
