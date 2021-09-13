from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AromaViewSet,
    BenefitViewSet,
    EffectViewSet,
    StrainViewSet,
    TerpeneViewSet,
)

router = DefaultRouter()
router.register("benefit", BenefitViewSet)
router.register("terpene", TerpeneViewSet)
router.register("effect", EffectViewSet)
router.register("aroma", AromaViewSet)
router.register("strain", StrainViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
