import random
import string

from django.db import models

from core.models import Base


class Reservation(Base):
    code_reservation = models.CharField(max_length=7, blank=True, unique=True)
    advertisement = models.ForeignKey('Advertisement', on_delete=models.CASCADE, related_name='reservations')
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    guest_count = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def generate_code_reservation(self):
        while True:
            letters = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
            numbers = ''.join(random.choice(string.digits) for i in range(3))
            code_reservation = letters + numbers
            if not Reservation.objects.filter(code_reservation=code_reservation).exists():
                return code_reservation

    def save(self, *args, **kwargs):
        if not self.code_reservation:
            self.code_reservation = self.generate_code_reservation()
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"Reservation #{self.code_reservation}"