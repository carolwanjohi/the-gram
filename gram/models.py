from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

# Default image for a new profile
DEFAULT = 'profile-pic/kakashi.jpg'

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

    # @classmethod
    # def get_single_profile(cls,user_id):
    #     '''
    #     Function that get's the profile of the specified user

    #     Args:
    #         user_id : id of specific user

    #     Return:
    #         single_profile : single Profile object belonging to user with specified id
    #     '''
    #     single_profile = Profile.objects.filter(user=user_id).all()[0]
    #     return single_profile

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

class Post(models.Model):
    '''
    Class that defines a Post made by a User on their Profile
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/")
    caption = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        '''
        Order posts with most recent at the top
        '''
        ordering = ['-post_date']

    # def save_post(self):
    #     '''
    #     Method to save a post to the database
    #     '''
    #     self.save()

    @classmethod
    def get_posts(cls):
        '''
        Function that gets all the posts in the database

        Returns:
            posts : list of all Post objects from the database
        '''
        posts = Post.objects.all()
        return posts

    @classmethod
    def get_profile_posts(cls,profile_id):
        '''
        Function that gets all the posts from a specific profile

        Returns:
            profile_posts : list of all the posts in a specific profile
        '''
        profile_posts = Post.objects.filter(profile=profile_id).all()
        return profile_posts

class Follow(models.Model):
    '''
    Class that store a User and Profile follow status
    '''
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)

    @classmethod
    def get_following(cls,user_id):
        '''
        Function that gets the Follow objects with a specific user id is get_following

        Return
            following : list of Follow objeect a User is following
        '''
        following =  Follow.objects.filter(user=user_id).all()
        return following










