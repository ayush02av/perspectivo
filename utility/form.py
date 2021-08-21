tabooChars = [
	'\'',
	'"'
]

def RequestFormValidate(request):
	for parameter in request:
		for char in tabooChars:
			if char in parameter:
				return False

	return True