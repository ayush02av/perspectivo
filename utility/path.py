user_profile_picture_path = 'profilepictures/profilepicture_{0}.png'
work_file_path = 'workfiles/{0}/work_{1}/{2}'
work_image_path = 'workfiles/{0}/work_{1}/{2}'

def User_Profile_Picture_Path(instance, filename):
	return user_profile_picture_path.format(instance.username)

def Work_File_Path(instance, filename):
	return work_file_path.format(instance.ByUser.username, instance.Title, filename)

def Work_Image_Path(instance, filename):
	return work_image_path.format(instance.ByUser.username, instance.Title, filename)