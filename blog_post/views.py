from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostAddForm, CommentAddForm
from .models import Post, Comment


class PostAddView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = PostAddForm(instance=request.user)
        return render(request, 'post_add.html', context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = PostAddForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = 'post saved'

        return render(request, 'post_add.html', context)


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentAddForm()
        context['comments'] = Comment.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['user'] = request.user.id
        data['post'] = kwargs['pk']
        comment_form = CommentAddForm(data)
        if comment_form.is_valid():
            comment = comment_form.save()
            comment.save()
        return self.get(request, *args, **kwargs)
