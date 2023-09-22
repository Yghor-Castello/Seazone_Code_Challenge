from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models.models_advertisement import Advertisement
from core.serializers.serializers_advertisement import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows advertisements to be viewed or edited.
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
 
    def destroy(self, request, *args, **kwargs):
        """
        Disable the DELETE method for this endpoint.

        This method returns a 405 Method Not Allowed response.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
