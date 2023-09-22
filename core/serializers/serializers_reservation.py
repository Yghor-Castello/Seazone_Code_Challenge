from rest_framework import serializers

from core.models.models_reservation import Reservation
from core.serializers.serializers_advertisement import AdvertisementSerializer


class ReservationSerializer(serializers.ModelSerializer):

    advertisement = AdvertisementSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'

    # Validando data de check-in vs data de check-out
    def validate(self, data):
        checkin_date = data.get('checkin_date')
        checkout_date = data.get('checkout_date')
        if checkin_date and checkout_date and checkin_date >= checkout_date:
            raise serializers.ValidationError({
                'checkout_date': 'Check-in date cannot be after or the same as the check-out date.'
            })
        return data