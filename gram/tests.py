from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Tag, Post, Follow, Comment, Like

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

    def test_get_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        gotten_profiles = Profile.get_profiles()

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profiles) == len(profiles))

    def test_get_other_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        gotten_profiles = Profile.get_other_profiles(self.james.id)

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profiles) < len(profiles))

    # def test_get_single_profile(self):
    #     '''
    #     Test case to check if a profile for a specific user are gotten from the database
    #     '''
    #     self.james = User(username="kiki")
    #     self.james.save()

    #     self.jane = User(username="ja-ne")
    #     self.jane.save()

    #     self.test_profile = Profile(user=self.jane,bio="Another Profile")

    #     gotten_profile = Profile.get_single_profile(self.jane.id)

    #     profiles = Profile.objects.all()

    #     self.assertTrue( len(gotten_profile) != len(profiles))

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
    Test case for the Post class
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

        gotten_profile = Post.get_profile_posts(self.jane.id)

        profiles = Post.objects.all()

        self.assertTrue( len(gotten_profile) == len(profiles))

class FollowTestClass(TestCase):
    '''
    Test case for the Follow class
    '''
    def test_instance(self):
        '''
        Test case to check if self.new_post in an instance of Follow class
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
        Test case to check if get following is getting profiles a specific user is following
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

class CommentTestClass(TestCase):
    '''
    Test case for the Comment class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comment(comment_content ='Python James is Muriuki who wrote Python content for Moringa School')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue( isinstance(self.new_comment, Comment) )

    def test_get_post_comments(self):
        '''
        Test case to check if get post comments is getting comments for a specific post
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.test_post = Post(user=self.jane,caption="Another Profile")

        self.test_comment = Comment(post=self.test_post,comment_content="Wow")

        gotten_comments = Comment.get_post_comments(self.test_post.id)

        comments = Comment.objects.all()

        # No comments were saved so expect True
        self.assertTrue( len(gotten_comments) == len(comments))

class LikeTestClass(TestCase):
    '''
    Test class to test the Like class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # Create a Like instance
        self.new_like = Like(likes_number=0 )

    def test_instance(self):
        '''
        Test case to check if self.new_like is an instance of Like
        '''

        self.assertTrue( isinstance( self.new_like, Like) )

    def test_get_post_likes(self):
        '''
        Test case to check if get post likes is getting the likes for a specific post
        '''

        gotten_likes = Like.get_post_likes(4990826417581240726341234)

        self.assertFalse( len(gotten_likes) , 1)

    def test_num_likes(self):
        '''
        Test to check if num likes is getting the number of likes a post is getting
        '''
        gotten_likes = Like.num_likes(123412312351123412341234123412341234)

        self.assertEqual( gotten_likes , 0)






    




