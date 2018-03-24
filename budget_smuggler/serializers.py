from rest_framework import serializers

from . import models


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(
            serializers.CurrentUserDefault()))

    class Meta:
        model = models.Expense
        read_only_fields = ['id', 'url']
        fields = read_only_fields + [
            'date',
            'cost',
            'item',
            'location',
            'notes',
            'user',
        ]
        extra_kwargs = {'url': {'view_name': 'expenses-detail'}}
