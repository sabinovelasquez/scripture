from django.shortcuts import get_object_or_404, render

from .models import Movie, Script

def detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'movies/detail.jade', {'movie': movie})

def index(request):
    latest_movie_list = Movie.objects.order_by('-pub_date')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'movies/index.jade', context)

def tag(request, tag):
    tag_name = tag
    latest_movie_list = Movie.objects.filter(tags__name__in=[tag])
    context = {'latest_movie_list': latest_movie_list, 'tag':tag }
    return render(request, 'movies/index.jade', context)
