from rest_framework import serializers
from mary.models import Aroma, Benefit, Effect, Strain, Terpene


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = "__all__"


class TerpeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terpene
        fields = "__all__"


class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = "__all__"


class AromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = "__all__"


class StrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strain
        fields = "__all__"
