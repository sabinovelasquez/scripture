from django.shortcuts import get_object_or_404, render

from .models import Movie

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.jade', {'movie': movie})

def index(request):
    latest_movie_list = Movie.objects.order_by('-pub_date')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'movies/index.jade', context)
