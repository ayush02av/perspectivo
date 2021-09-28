from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.validators

import pytz, os, glob
from utility import path

from django.utils import timezone

class User(AbstractUser):
	about = models.TextField(max_length=500, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	number = models.CharField(max_length=10, null=True, blank=True)
	profile_picture = models.ImageField(upload_to=path.User_Profile_Picture_Path, null=True, blank=True)
	password = models.CharField(max_length=100, editable=False)

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
    #     if self.profile_picture.__str__() != '':
    #         path = self.profile_picture.path
    #         path = path.replace(path.split(os.sep)[-1], '')
    #         path = glob.glob(path + '*.png')
    #         path.remove(self.profile_picture.path)
    #         for file in path:
    #             os.remove(file)

class Genre(models.Model):
	GenreName = models.CharField(max_length=20)

	def __str__(self):
		return self.GenreName


class WorkType(models.Model):
	TypeName = models.CharField(max_length=20)
	TypeDescription = models.CharField(max_length=50)

	def __str__(self):
		return self.TypeName

class Work(models.Model):
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='WorkByUser')
	DateTimePosted = models.DateTimeField(default=timezone.now, editable=True)
	Title = models.CharField(max_length=200)
	Content = models.TextField(null=True, blank=True)
	MainLiner = models.CharField(max_length=500, null=True, blank=True)
	File = models.FileField(upload_to=path.Work_File_Path, null=True, blank=True)
	Image = models.ImageField(upload_to=path.Work_Image_Path, null=True, blank=True)

	PUBLIC = 'PUBLIC'
	PROTECTED = 'PROTECTED'
	PRIVATE = 'PRIVATE'

	ListingChoices = [
		(PUBLIC, 'Public - Anyone on the internet can view'),
		(PROTECTED, 'Protected - Only people registered with Perspectivo can view'),
		(PRIVATE, 'Private - Only you can view'),	
	]
	ListingType = models.CharField(max_length=9, choices=ListingChoices, default=PUBLIC)

	WorkType = models.ForeignKey(WorkType, on_delete=models.CASCADE, related_name='WorkType')
	Genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL, related_name='WorkGenre')

	Rating = models.IntegerField(default=0)

	def __str__(self):
		return self.ByUser.__str__() + ' : ' + self.Title + ' on ' + self.DateTimePosted.__str__()

class Review(models.Model):
	ForWork = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='ReviewForWork')
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ReviewByUser')
	DateTimePosted = models.DateTimeField(default=timezone.now, editable=True)
	Title = models.CharField(max_length=200)
	Text = models.TextField(null=True, blank=True)
	File = models.FileField(upload_to='workfiles/', null=True, blank=True)

	def __str__(self):
		return self.ByUser.__str__() + ' on ' + self.ForWork.__str__() + ' says, ' + self.Title

class Vote(models.Model):
	ForWork = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='VoteForWork')
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='VotewByUser')

	VoteChoices = [
		('UPVOTE', 'UPVOTE'),
		('DOWNVOTE', 'DOWNVOTE'),
	]
	Vote = models.CharField(max_length=9, choices=VoteChoices)

	def __str__(self):
		return self.Vote.__str__() + ' by ' + self.ByUser.__str__() + ' on ' + self.ForWork.__str__()