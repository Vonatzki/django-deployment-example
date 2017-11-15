from django.db import models
from django.contrib.auth.models import User

### Create your models here.

# User Model Extension
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)

	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	class Meta:
		verbose_name= 'User Profile'
		verbose_name_plural='User Profiles'

	def __str__(self):
		return self.user.username