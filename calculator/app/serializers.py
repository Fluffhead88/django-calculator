from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Calculator

class CalculatorSerializer(ModelSerializer):

    class Meta:
        fields = ["id", 'operand_one', 'operand_two', 'operator', 'result', 'created' "owner"]
        read_only_fields = ["owner"]
        model = Calculator
