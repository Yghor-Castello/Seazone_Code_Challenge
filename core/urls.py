from django.urls import path, include
from rest_framework.routers import SimpleRouter

from core.views import AdvertisementViewSet, RealtyViewSet, ReservationViewSet


router = SimpleRouter()

router.register('advertisement', AdvertisementViewSet, basename='advertisement')
router.register('realty', RealtyViewSet, basename='realty')
router.register('reservation', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
]