from rest_framework import viewsets

from core.models.models_realty import Realty
from core.serializers.serializers_realty import RealtySerializer


class RealtyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows real estate listings to be viewed or edited.
    """
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer
    lookup_field = 'code_realty'
