from rest_framework import authentication
from mary.models import Aroma, Benefit, Effect, Strain, Terpene
from .serializers import (
    AromaSerializer,
    BenefitSerializer,
    EffectSerializer,
    StrainSerializer,
    TerpeneSerializer,
)
from rest_framework import viewsets


class BenefitViewSet(viewsets.ModelViewSet):
    serializer_class = BenefitSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Benefit.objects.all()


class TerpeneViewSet(viewsets.ModelViewSet):
    serializer_class = TerpeneSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Terpene.objects.all()


class EffectViewSet(viewsets.ModelViewSet):
    serializer_class = EffectSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Effect.objects.all()


class AromaViewSet(viewsets.ModelViewSet):
    serializer_class = AromaSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Aroma.objects.all()


class StrainViewSet(viewsets.ModelViewSet):
    serializer_class = StrainSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Strain.objects.all()
