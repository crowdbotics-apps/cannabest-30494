from django.contrib import admin
from .models import Aroma, Benefit, Effect, Strain, Terpene

admin.site.register(Benefit)
admin.site.register(Terpene)
admin.site.register(Effect)
admin.site.register(Aroma)
admin.site.register(Strain)

# Register your models here.
