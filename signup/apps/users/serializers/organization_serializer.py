from rest_framework import serializers
from ..models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    '''
    组织架构序列化
    '''
    type = serializers.ChoiceField(choices=Organization.organization_type_choices, default='company')

    class Meta:
        model = Organization
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    """
    用户
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    type = serializers.ChoiceField(choices=Organization.organization_type_choices, default='company')


class OrganizationUserTreeSerializer(serializers.ModelSerializer):
    '''
    组织架构树序列化
    '''
    children = UserSerializer(many=True, read_only=True, source='user_department')

    class Meta:
        model = Organization
        fields = ('id', 'name', 'pid','sort', 'children')


class OrganizationGraTreeSerializer(serializers.ModelSerializer):
    '''
    组织架构树序列化
    '''
    class Meta:
        model = Organization
        fields = ('id', 'name', 'pid')
