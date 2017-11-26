from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Profile, Tag, Post, Follow
from .forms import NewsPostForm

# Create your views here.
@login_required(login_url='/accounts/register')
def timeline(request):
    '''
    View function to display the timeline page for an authenticated logged in user
    '''
    current_user = request.user

    title = 'Home'

    message = 'Timeline Page'

    return render(request, 'all-posts/timeline.html', {"title": title, "message": message, "user":current_user})

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
    View function to display a form for creating a post to a logged in authenticated user 
    '''
    current_user = request.user

    current_user_profile = current_user.profile

    profiles = Profile.get_other_profiles(current_user.id)

    title = f'{current_user.username} explore'

    return render(request,'all-posts/explore.html',{"title":title,"profiles":profiles})






