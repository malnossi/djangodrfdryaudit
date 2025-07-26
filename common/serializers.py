# common/serializers.py
from rest_framework import serializers


class AuditSerializerMixin(serializers.Serializer):
    created_by = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    )
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["created_by"] = instance.created_by.id
        rep["updated_by"] = instance.updated_by.id
        return rep
