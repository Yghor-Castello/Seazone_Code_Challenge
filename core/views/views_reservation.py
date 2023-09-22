from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models.models_reservation import Reservation
from core.serializers.serializers_reservation import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed, created, updated, or deleted.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        """
        Create a new reservation.

        Checks if the check-in date is before the check-out date. If not, returns a 400 Bad Request response.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The HTTP response indicating success or failure.
        """
        checkin_date = request.data.get('checkin_date')
        checkout_date = request.data.get('checkout_date')
        if checkin_date >= checkout_date:
            return Response({"detail": "Check-in date cannot be after or the same as the check-out date."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Disable the UPDATE method for this endpoint.

        This method returns a 405 Method Not Allowed response.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The HTTP response indicating that the update method is not allowed.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)