from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie

def detail(request, movie_id):
  return HttpResponse("Movie %s." % movie_id)


def index(request):
    latest_premise_list = Premise.objects.order_by('-pub_date')[:5]
    context = {'latest_premise_list': latest_premise_list}
    return render(request, 'premises/index.jade', context)