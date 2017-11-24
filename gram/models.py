from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

# Default image for a new profile
DEFAULT = 'static/images/kakashi.jpg'

# Create your models here.
class Profile(models.Model):
    '''
    Class to define a user's profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile-pic/", blank=True, default=DEFAULT)

    def __str__(self):
        '''
        Display for profiles in profile table
        '''
        return self.user.username

    @classmethod
    def get_profiles(cls):
        '''
        Fucntion that gets all the profiles in the app

        Return
            profiles : list of all Profile obejcts in the database
        '''
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def get_single_profile(cls,user_id):
        '''
        Function that get's the profile of the specified user

        Args:
            user_id : id of specific user

        Return:
            single_profile : single Profile object belonging to user with specified id
        '''
        single_profile = Profile.objects.filter(user=user_id).all()
        return single_profile

    # @classmethod
    # def set_profile_pic_to_default(self):
    #     '''
    #     Function that set's a profile pictue back to the default one
    #     '''
    #     self.profile_pic.delete(save=False)  
    #     self.profile_pic = DEFAULT
    #     self.save()

# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Tag(models.Model):
    '''
    Class that defines categories of posts and tags on posts
    '''
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def save_tag(self):
        '''
        Method to save a new tag to the database
        '''
        self.save()

    def delete_tag(self):
        '''
        Method to delete a tag from the database
        '''
        self.delete()

    @classmethod
    def get_tags(cls):
        '''
        Method that gets all tags from the database

        Returns:
            gotten_tags : list of tag objects from the database
        '''
        gotten_tags = Tag.objects.all()
        return gotten_tags









