from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Profile, Tag, Post, Follow, Comment, Like
from .forms import NewsPostForm, NewCommentForm

# Create your views here.
@login_required(login_url='/accounts/register')
def timeline(request):
    '''
    View function to display the timeline page for an authenticated logged in user
    '''
    current_user = request.user

    title = 'Home'

    following = Follow.get_following(current_user.id)

    posts = Post.get_posts()

    following_posts = []

    for follow in following:

        for post in posts:

            if follow.profile == post.profile:

                following_posts.append(post)

    comments = Comment.objects.all()

    post_comments = []

    for comment in comments:

        for post in posts:

            if comment.post.id == post.id:

                post_comments.append(comment)

    likes = []
    
    for post in following_posts:

        likes.append(Like.num_likes(post.id))

    return render(request, 'all-posts/timeline.html', {"title": title, "following": following, "user":current_user, "following_posts":following_posts,"post_comments":post_comments,"likes":likes})

@login_required(login_url='/accounts/register')
def profile(request,id):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        posts = Post.objects.filter(user=current_user.id)

        return render(request, 'all-posts/my-profile.html', {"title":title,"current_user":current_user,"posts":posts})

    except DoesNotExists:
        raise Http404()

    # print(single_profile)
    # print(current_user)
    # title = f'{single_profile.user.username}'

    # if single_profile.user.id != current_user.id :
            
    #     '''
    #     If the logged in user is not the owner of the profile display the following
    #     '''
    #     message = f'{current_user.username} is visiting {single_profile.user.username}\'s profile'
    #     return render(request, 'all-posts/following-profile.html', {"title":title,"current_user":current_user,"message":message})

    # '''
    # If the logged in user is the owner of the profile display the following
    # '''
    # message = f'{current_user.username}\'s profile'
    # return render(request, 'all-posts/my-profile.html', {"title":title,"current_user":current_user,"message":message})

@login_required(login_url='/accounts/register')
def new_post(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user 
    '''
    current_user = request.user

    current_profile = current_user.profile

    if request.method == 'POST':

        form = NewsPostForm(request.POST, request.FILES)

        if form.is_valid:

            post = form.save(commit=False)

            post.user = current_user

            post.profile = current_profile

            post.save()

            return redirect(profile, current_user.id)

    else:

        form = NewsPostForm()

    title = 'Create Post'

    return render(request,'all-posts/new-post.html', {"form":form})

@login_required(login_url='/accounts/register')
def explore(request,id):
    '''
    View function to display a list of profiles that the current user is not following
    '''
    current_user = request.user

    current_user_profile = current_user.profile

    profiles = Profile.get_other_profiles(current_user.id)

    title = f'{current_user.username} explore'

    return render(request,'all-posts/explore.html',{"title":title,"profiles":profiles})

@login_required(login_url='/accounts/register')
def follow(request,id):
    '''
    View function to add a profile to the current user's timeline
    '''
    current_user = request.user

    follow_profile = Profile.objects.get(id=id)

    following = Follow(user=current_user, profile=follow_profile)

    following.save()

    return redirect(timeline)

@login_required(login_url='/accounts/register')
def comment(request,id):
    '''
    View function to display a form for creating a comment on a post
    '''
    current_user = request.user

    current_post = Post.objects.get(id=id)

    if request.method == 'POST':

        form = NewCommentForm(request.POST)

        if form.is_valid:

            comment = form.save(commit=False)

            comment.user = current_user

            comment.post = current_post

            comment.save()

            return redirect(timeline)

    else:

        form = NewCommentForm()

    title = f'Comment {current_post.user.username}\'s Post'

    return render(request,'all-posts/new-comment.html', {"title":title,"form":form,"current_post":current_post})

@login_required(login_url='/accounts/register')
def like(request,id):
    '''
    View function add a like to a post the current user has liked
    '''
    current_user = request.user

    current_post = Post.objects.get(id=id)

    like = Like(user=current_user,post=current_post,likes_number=1)

    like.save()

    return redirect(timeline)







