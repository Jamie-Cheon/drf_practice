from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


"""
ModelSerializer : Simply a shortcut for creating serializer classes
                - an automatically determined set of fields
                - simple default implementations for the create(), update() methods
"""


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'price', 'owner', 'title', 'code', 'linenos', 'language', 'style']

