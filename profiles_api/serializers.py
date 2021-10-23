from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
	"""Serializers a name for testing out APIView"""
	name = serializers.CharField(max_length=10)
