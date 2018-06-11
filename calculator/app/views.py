from django.shortcuts import render

from rest_framework import generics
from app.models import Calculator
from app.serializers import CalculatorSerializer
from app.permissions import IsOwnerOrReadOnly

class CalculatorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer

    def perform_create(self, serializer):
        serializer.result = serializer.operand_one, serializer.operator, serializer.operand_two
        serializer.save(owner=self.request.user)
        return Response(result)


class CalculatorRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer
