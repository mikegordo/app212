from django.urls import path

from app212.views import TickDetails

urlpatterns = [
    path('tick/<int:id>', TickDetails.as_view()),
    path('tick', TickDetails.as_view()),
]
