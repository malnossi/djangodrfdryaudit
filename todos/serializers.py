from rest_framework import serializers
from common.serializers import AuditSerializerMixin
from .models import Todo


class TodoSerializer(AuditSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )
