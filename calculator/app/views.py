from django.shortcuts import render

from rest_framework import generics
from app.models import Calculator
from app.serializers import CalculatorSerializer
from app.permissions import IsOwnerOrReadOnly

class CalculatorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer

    def perform_create(self, serializer):
        result = serializer.validated_data
        x = 0
        if result['operator'] == "+":
            x = (result['operand_one'] + result['operand_two'])
        elif result['operator'] == "-":
            x = (result['operand_one'] - result['operand_two'])
        elif result['operator'] == "*":
            x = (result['operand_one'] * result['operand_two'])
        elif result['operator'] == "/":
            x = (result['operand_one'] / result['operand_two'])
        serializer.save(owner=self.request.user, result=x)



class CalculatorRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer
