from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Tag,Post, Follow

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of Profile class
        self.new_profile = Profile(bio="I am Groot")

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue( isinstance(self.new_profile, Profile) )
        User.objects.all().delete()

    def test_get_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        gotten_profiles = Profile.get_profiles()
        profiles = Profile.objects.all()
        self.assertTrue( len(gotten_profiles) == len(profiles))

    def test_get_single_profile(self):
        '''
        Test case to check if a profile for a specific user are gotten from the database
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        gotten_profile = Profile.get_single_profile(self.jane.id)

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profile) != len(profiles))

class TagTestClass(TestCase):
    '''
    Test case for Tag class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a Tag instance before each test
        '''
        # Create a Tag instance
        self.new_tag = Tag(name='Python')

    def test_instance(self):
        '''
        Test case to check if self.new_tag in an instance of Tag class
        '''
        self.assertTrue( isinstance(self.new_tag, Tag) )

    def test_save_tag(self):
        '''
        Test case to check is a tag is saved in the database
        '''
        self.new_tag.save_tag()
        gotten_tags = Tag.objects.all()
        self.assertTrue( len(gotten_tags) > 0 )

    def test_delete_tag(self):
        '''
        Test case to check if a tag is deleted from the database
        '''
        self.new_tag.save_tag()
        gotten_tags = Tag.objects.all()
        self.new_tag.delete_tag()
        self.assertTrue( len(gotten_tags) == 0 )

    def test_get_tags(self):
        '''
        Test case to check if all tags are gotten from the database
        '''
        self.new_tag.save_tag()
        gotten_tags = Tag.get_tags()
        existing_tags = Tag.objects.all()
        self.assertTrue( len(gotten_tags) == len(existing_tags))

class PostTestClass(TestCase):
    '''
    Test case for the Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''

        # Create a Post instance
        self.new_post = Post(caption ='Python James is Muriuki who wrote Python content for Moringa School')

    def test_instance(self):
        '''
        Test case to check if self.new_post in an instance of Post class
        '''
        self.assertTrue( isinstance(self.new_post, Post) )

    def test_get_posts(self):
        '''
        Test case to check if all posts are gotten from the database
        '''
        gotten_posts = Post.get_posts()
        posts = Post.objects.all()
        self.assertTrue( len(gotten_posts) == len(posts))

    def test_get_profile_posts(self):
        '''
        Test case to check if all posts for a specific profile are gotten from the database
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.test_post = Post(user=self.jane,caption="Another Profile")

        gotten_profile = Profile.get_single_profile(self.jane.id)

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profile) != len(profiles))

class FollowTestClass(TestCase):
    '''
    Test case for the Profile class
    '''
    def test_instance(self):
        '''
        Test case to check if self.new_post in an instance of Post class
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.new_follow = Follow(user=self.jane, profile=self.test_profile)

        self.assertTrue( isinstance(self.new_follow, Follow) )

    def test_get_following(self):
        '''
        Test case to test get following is getting profiles a specific user is following
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.test_post = Post(user=self.jane,caption="Another Profile")

        self.new_follow = Follow(user=self.jane, profile=self.test_profile)

        gotten_following = Follow.get_following(self.jane.id)

        followings = Follow.objects.all()

        self.assertTrue( len(gotten_following) == len(followings))






    




