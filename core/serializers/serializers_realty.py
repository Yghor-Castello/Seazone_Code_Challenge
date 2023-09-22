from rest_framework import serializers

from core.models.models_realty import Realty


class RealtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Realty
        fields = '__all__'

