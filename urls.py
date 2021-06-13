from django.urls import path
from .views import PLAYGAME


urlpatterns = [

    path('', PLAYGAME.as_view())
]