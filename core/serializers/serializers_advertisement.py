from rest_framework import serializers
from core.models.models_advertisement import Advertisement
from core.serializers.serializers_realty import RealtySerializer
from core.models.models_realty import Realty

class AdvertisementSerializer(serializers.ModelSerializer):
    realty = serializers.PrimaryKeyRelatedField(queryset=Realty.objects.all(), write_only=True)
    realty_detail = RealtySerializer(source='realty', read_only=True)

    class Meta:
        model = Advertisement
        fields = '__all__'
