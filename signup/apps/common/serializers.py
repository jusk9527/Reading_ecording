# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       jusk?
   date：          2019/9/15
-------------------------------------------------
   Change Activity:
                   2019/9/15:
-------------------------------------------------
"""

from rest_framework import serializers
from .models import ProList

class ProListSerializer(serializers.ModelSerializer):
    """
    常见问题
    """
    class Meta:
        model = ProList
        fields = "__all__"