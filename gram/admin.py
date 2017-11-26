from django.contrib import admin
from .models import Profile, Tag, Post, Follow, Comment, Like

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    '''
    Customise model in admin page
    '''
    filter_horizontal = ('tags',)

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)



