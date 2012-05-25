from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='users')	
	first_name = models.CharField(max_length = 50, blank=True, null=True)
	last_name = models.CharField(max_length = 50, blank=True, null=True)	
	image_profile = models.ImageField(upload_to = 'image', blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	location = models.CharField(max_length = 50, blank=True, null=True)
	biography = models.CharField(max_length = 150, blank=True, null=True)
	following = models.ManyToManyField('Profile',  related_name='followers', blank=True, null=True)
	

	def __unicode__(self):
			return 'User: %s - %s %s' % (self.pk, self.last_name, self.first_name)

def get_profile(user):
	if not hasattr(user, '_profile_cache'):
		profile, created = Profile.objects.get_or_create(user=user)
		user.profile_cache = profile
	return user.profile_cache

User.get_profile=get_profile
			

class Tweet(models.Model):
	owner = models.ForeignKey('Profile' , related_name='tweets')
	status = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add=True)

