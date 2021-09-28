from rest_framework.response import Response

def Api_Get_Response(serializer, queryset=[], many=True):
	serializer = serializer(queryset, many=many)
	return Response(serializer.data)

def Api_Update_Response(serializer, request, instance):
	serializer = serializer(instance=instance, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

def Api_Post_Response(serializer, request):
	serializer = serializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)