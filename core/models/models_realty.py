import random
import string

from django.db import models

from core.models import Base


class Realty(Base):
    code_realty = models.CharField(max_length=7, blank=True, unique=True)
    guest_limit = models.PositiveIntegerField()
    bathroom_count = models.PositiveIntegerField()
    accepts_pets = models.BooleanField(default=False)
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()

    class Meta:
        verbose_name = "Realty"
        verbose_name_plural = "Realties"

    def generate_code_realty(self):
        while True:
            letters = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
            numbers = ''.join(random.choice(string.digits) for i in range(3))
            code_realty = letters + numbers  
            if not Realty.objects.filter(code_realty=code_realty).exists():
                return code_realty

    def save(self, *args, **kwargs):
        if not self.code_realty:  
            self.code_realty = self.generate_code_realty()
        super(Realty, self).save(*args, **kwargs)

    def __str__(self):
        return f"Realty #{self.code_realty}"
