from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

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
    View function to display the profile of either the logged in user or logged in user viewing another person's profile
    '''
    current_user = request.user
    title = f'{current_user.username}'
    return render(request, 'all-posts/profile.html', {"title":title,"current_user":current_user})



