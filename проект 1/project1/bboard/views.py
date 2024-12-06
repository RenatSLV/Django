from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from .forms import BbForm
from .models import *

class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index_html')
    # Второй метод  success_url = '/bboard/html/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    s = "Список объевлений\r\n"
    bb = Bb.objects.order_by("-published")
    for b in bb:
        s += b.title + '\r\n' + b.content + '\r\n'
    return HttpResponse(s, content_type="text/plain; charset=utf-8")

def get_by_slug(request, slug):
    crypto=Crypto.objects.get(slug=slug)
    return render(request, 'cripto.html', {'crypto': crypto})

def get_comment_by_id(request, id):
    comments = Comment.objects.get(id=id)
    return render(request, 'comment.html', {'comment': comments})

def delete_comment_by_id(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()

    comments = Comment.objects.all()
    return render(request, 'comment2.html', {'comments': comments})


def about_me(request):
    return HttpResponse("My name is Renat and you ?")


def index_html(request):
    # template = loader.get_template('index.html')
    bb = Bb.objects.order_by("-published")
    rubrics = Rubric.objects.all()
    context = {'bb': bb, 'rubrics':rubrics}
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)

def by_rubric(request, rubric_id):
    bb = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {'bb':bb, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return  render(request, 'by_rubric.html', context)