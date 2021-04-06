from django.contrib import admin
from musicboxapp.models import User
from musicboxapp.models import Album, Review
from musicboxapp.models import Comment

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class CommentAdmin(admin.ModelAdmin):
    display = ('User', 'Album', 'Comment', 'Date_Posted')
    filter_list = ('Date_Posted')
    search = ('User', 'Comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(User)
admin.site.register(Album)
admin.site.register(Comment)
admin.site.register(Review)

