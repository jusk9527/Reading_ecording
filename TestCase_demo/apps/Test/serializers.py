from rest_framework import serializers

from .models import HomeWork


class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = ('school_name', 'class_name', 'student_name', 'name')

    school_name = serializers.CharField(source='student_id.class_id.school_id.name', read_only=True)
    class_name = serializers.CharField(source='student_id.class_id.name', read_only=True)
    student_name = serializers.CharField(source='student_id.name', read_only=True)