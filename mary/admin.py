from django.contrib import admin
from .models import Aroma, Benefit, Effect, Terpene

admin.site.register(Benefit)
admin.site.register(Terpene)
admin.site.register(Effect)
admin.site.register(Aroma)

# Register your models here.
