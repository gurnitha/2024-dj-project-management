from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
	name = models.CharField(max_length=200,null=True,blank=True)
	email =models.EmailField(blank=True,null=True)
	photo =models.ImageField()
	bio = models.TextField(null=True,blank=True)

	def __str__(self):
		return str(self.user)


'''
The function create_user_profile takes the following arguments:
● sender 	: The model sending the signal, in our case, the user model,
● instance 	: The user instance created
● created 	: A boolean checking if the instance was created; 
              if True, a profile object is created.
● kwargs 	: Any other keyword arguments that may be passed.
'''
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


'''
After defining the signal receiver, we need to connect the receiver to a signal. Here is how to
connect it
'''
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
