from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class ExpenseViewSet(ModelViewSet):
    queryset = models.Expense.objects.none()
    serializer_class = serializers.ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Expense.objects.filter(user=self.request.user)
