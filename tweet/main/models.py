from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	user = models.OneToOneField(User)	
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)	
	image_profile = models.ImageField(upload_to = 'image')
	birth_date = models.DateField()
	location = models.CharField(max_length = 50)
	biography = models.CharField(max_length = 150)
	following = models.ManyToManyField('User',  related_name='followers', blank='True')
	

	def __unicode__(self):
			return 'User: %s - %s %s' % (self.pk, self.last_name, self.first_name)

def get_profile(user):
	if not hasattr(user, '_profile_cache'):
		profile, created = Perfil.objects.get_or_create(user=user)
		user.profile_cache = profile
	return user.profile_cache

User.get_profile=get_profile
			

class Tweet(models.Model):
	owner = models.ForeignKey('User' , related_name='tweets')
	status = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add=True)

