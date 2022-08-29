from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RestaurantsViewSet


app_name = 'api_restaurants'

router = DefaultRouter()

router.register(
    'restaurants',
    RestaurantsViewSet,
    basename='restaurants'
)

urlpatterns = [
    path('', include(router.urls)),
]
