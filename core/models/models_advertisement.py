from django.db import models

from core.models import Base


class Advertisement(Base):
    realty = models.ForeignKey('Realty', on_delete=models.CASCADE, related_name='advertisements')
    platform_name = models.CharField(max_length=255)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        return f"Advertisement #{self.id} - {self.platform_name}"
