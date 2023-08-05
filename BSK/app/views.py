from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
class HomeListView(ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'abouts'
    template_name = 'index.html'
    #
    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     context['projects'] = Project.objects.all()
    #     context['programs'] = Program.objects.all()
    #     context['aboutkeus'] = AboutKEU.objects.all()
    #     context['pages'] = BlankPage.objects.all()
    #     context['news'] = News.objects.order_by('-date')[:3]
    #     context['abouts'] = About.objects.all()
    #     context['aboutkeu'] = AboutKEU.objects.all()[0]
    #     return context
#
# class NewsListView(ListView):
#     model = News
#     queryset = News.objects.all()
#     context_object_name = 'news'
#     template_name = 'news.html'
#
#     def get_context_data(self, **kwargs):
#
#         context = super().get_context_data(**kwargs)
#         context['projects'] = Project.objects.all()
#         context['programs'] = Program.objects.all()
#         context['aboutkeus'] = AboutKEU.objects.all()
#         context['aboutkeu'] = AboutKEU.objects.all()[0]
#         context['abouts'] = About.objects.all()
#         return context
#
#
# class DetailNews(DetailView):
#     model = News
#     context_object_name = 'news'
#     template_name = 'detail_news.html'
#
#     def get_context_data(self, **kwargs):
#
#         context = super().get_context_data(**kwargs)
#         context['projects'] = Project.objects.all()
#         context['programs'] = Program.objects.all()
#         context['aboutkeus'] = AboutKEU.objects.all()
#         context['aboutkeu'] = AboutKEU.objects.all()[0]
#         context['abouts'] = About.objects.all()
#         return context
