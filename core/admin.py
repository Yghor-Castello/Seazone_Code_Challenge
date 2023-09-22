from django.contrib import admin

import core.models as models


admin.site.register(models.Advertisement)
admin.site.register(models.Realty)
admin.site.register(models.Reservation)