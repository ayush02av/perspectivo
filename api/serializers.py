from rest_framework import serializers

from database.models import *

class User_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = User
		fields = (
				"username",
				"first_name",
				"last_name",
				"email"
			)

class Work_Serializer(serializers.ModelSerializer):
	ByUser = User_Serializer(many=False, read_only=True)
	class Meta(object):
		model = Work
		fields = (
			"Title",
			"ByUser",
			"Content",
			"Image"
			)

class Glipmses_Serializer(serializers.ModelSerializer):
	ByUser = User_Serializer(many=False, read_only=True)
	class Meta(object):
		model = Work
		fields = (
			"Title",
			"ByUser",
			"Rating",
			"MainLiner"
			)