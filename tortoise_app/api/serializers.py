from rest_framework import serializers
from base.models import Plan
from base.models import Promotions
from base.models import CustomerGoals

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    planId = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=Plan.objects.all()
    )
    class Meta:
        model = Promotions
        fields = '__all__'

class CustomerGoalsSerializer(serializers.ModelSerializer):
    planId = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=Plan.objects.all()
    )
    class Meta:
        model = CustomerGoals
        fields = '__all__'