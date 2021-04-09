from django.shortcuts import render
from musicboxapp.models import User, Album, Review, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.utils.decorators import method_decorator
import random
#from musicboxapp.bing_search import run_query

class HomepageView(View):
    def get(self, request):
        albums_recently_reviewed = Album.objects.order_by('Date_Of_Review')[:3]
        albums_recently_released = Album.objects.order_by('Release')[:3]
        context_dict = {}
        context_dict['recently_reviewed'] = albums_recently_reviewed
        context_dict['recent_releases'] = albums_recently_released

        response = render(request, 'musicBox/homepage.html', context=context_dict)
        return response

class AlbumView(View):
    def get(self, request, album_name_slug):
        context_dict = {}

        try:
            album = Album.objects.get(slug=album_name_slug)
            reviews = Review.objects.filter(album=album).order_by("-Date_Of_Review")

            context_dict['reviews'] = reviews
            context_dict['album'] = album
        except Album.DoesNotExist:
            context_dict['album'] = None
            context_dict['reviews'] = None

        return render(request, 'musicBox/album.html', context=context_dict)

class ReviewView(View):
    def get(self, request, album_name_slug):
        context_dict = {}

        try:
            review = Review.objects.get(Album=album_name_slug)
            context_dict['review'] = review
        except Album.DoesNotExist:
            album = None

        if album is None:
            return redirect('/musicboxapp/')

        return render(request, 'musicBox/review.html', context=context_dict)

class AddReviewView(View):
    def context_builder(self, album_name_slug):
        context = {}
        try:
            album = Album.objects.get(slug=album_name_slug)
        except Album.DoesNotExist:
            album = None

        if album is None:
            return redirect('/musicboxapp/')

        return context

    @method_decorator(login_required)
    def get(self, request, album_name_slug):
        context = self.context_builder(album_name_slug)

        return render(request, 'music/add_review.html', context=context)

    @method_decorator(login_required)
    def post(self, request, album_name_slug):
        if request.user.is_authenticated:
            form = ReviewForm(request.POST or None)

            if form.is_valid():
                review = form.save(commit=False)
                review.Review = request.POST["Review"]
                review.Rating = request.POST["Rating"]
                review.User = request.user
                review.Album = Album
                review.save()

                return redirect(reverse('musicBox:album', kwargs={'album_name_slug': album_name_slug}))
            else:
                print(form.errors)

        context = this.context_builder(album_name_slug)
        context['form'] = form

        return render(request, 'musicBox/add_review.html', context=context)

    # def add_review(request, album_name_slug):
    #     try:
    #         album = Album.objects.get(slug=album_name_slug)
    #     except Album.DoesNotExist:
    #         album = None
    #
    #     if album is None:
    #         return redirect('/musicboxapp/')
    #
    #     if request.user.is_authenticated:
    #         if request.method == "POST":
    #             form = ReviewForm(request.POST or None)
    #
    #             if form.is_valid():
    #                 review = form.save(commit=False)
    #                 review.Review = request.POST["Review"]
    #                 review.Rating = request.POST["Rating"]
    #                 review.User = request.user
    #                 review.Album = album
    #                 review.save()
    #
    #                 return redirect(reverse('musicboxapp:album', kwargs={'album_name_slug': album_name_slug}))
    #             else:
    #                 print(form.errors)
    #
    #     context_dict = {'form': form, 'album': album}
    #     return render(request, 'musicboxapp/add_review.html', context=context_dict)

class DeleteReviewView(View):
    @method_decorator(login_required)
    def delete_review(self, request, album_name_slug, review_id):
        if request.user.is_authenticated:
            album = Album.objects.get(slug=album_name_slug)
            review = Review.objects.get(album=album, id=review_id)

            if request.method == "POST":
                review.delete()

            return redirect("musicBox:album", kwargs={'album_name_slug': album_name_slug})
        else:
            return redirect("users:login")

class AddCommentView(View):
    @method_decorator(login_required)
    def add_comment(self, request, album_name_slug):
        template = 'add_comment.html'
        album = Album.objects.get(slug=album_name_slug)
        comment = album.comment.filter(active=True)
        new_comment = None

        if request.user.is_authenticated:
            if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    new_comment = form.save(commit=False)
                    new_comment.album = album
                    new_comment.save()
            else:
                form = CommentForm()
        else:
            return redirect('users:login')

        context_dict = {'album': album, 'comment': comment, 'new_comment': new_comment, 'form': form}
        return render(request, template, context=context_dict)


class SearchView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

# def search(request):
#     result_list = []
#
#     if request.method == "POST":
#         query = request.POST['query'].strip()
#         if query:
#             result_list = run_query(query)
#
#     return render(request, 'musicboxapp/search.html', {'result_list': result_list})

class BrowseGenresView(View):
    def get(self, request):
        context = {}

        return render(request, 'musicBox/browse_genres.html', context=context)

class TrendingPageView(View):
    def get(self, request):
        context = {}

        return render(request, 'musicBox/trending.html', context=context)

class PopularPageView(View):
    def get(self, request):
        context = {}

        return render(request, 'musicBox/popular.html', context=context)

class SurprisePageView(View):
    pass
