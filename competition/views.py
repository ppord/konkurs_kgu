from django.shortcuts import render
from annoying.decorators import render_to
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from competition.models import TextIdea, DesignIdea

class TextIdeaList(ListView):
    model = TextIdea
    paginate_by = 20
    template_name = 'textlist.html'


class DesignIdeaList(ListView):
    model = DesignIdea
    paginate_by = 20
    template_name = 'imglist.html'


@render_to('index.html')
def index(request):

    pass

# Create your views here.
