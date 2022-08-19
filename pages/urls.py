from django.urls import path
from .views import AboutusRetrieveAPIView, ListCreateAboutus,AboutusDelete
urlpatterns = [
    path('',ListCreateAboutus.as_view(),name='About'),
    path('get/<int:pk>',AboutusRetrieveAPIView.as_view()),
    path('delete/<int:pk>',AboutusDelete.as_view())


]