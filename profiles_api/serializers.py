from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializar un campo para probar nuestra APIView """
    name = serializers.CharField(max_length=10)
