from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login')
def timeline(request):
    '''
    View function to display the timeline page for an authenticated logged in user
    '''
    title = 'Home'
    message = 'Timeline Page'
    return render(request, 'all-posts/timeline.html', {"title": title, "message": message})


