from rest_framework import serializers

from database.models import *

# class Monthly_Budget_Serializer(serializers.ModelSerializer):
# 	class Meta(object):
# 		model = MonthlyBudget
# 		fields = "__all__"

class Work_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = Work
		fields = "__all__"