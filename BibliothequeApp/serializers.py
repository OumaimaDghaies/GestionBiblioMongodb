from rest_framework import serializers
from .models import Abonne, Document, Emprunt

class AbonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonne
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'
