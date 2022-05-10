from rest_framework import serializers
from snippets.models import *

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['code', 'libelle', 'prix_achat', 'date_create', 'date_peremtion']

