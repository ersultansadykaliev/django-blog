# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Post, Comment
from .forms import CommentForm
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.filter(approved=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            messages.success(request, 'Ваш комментарий отправлен на модерацию!')
            return redirect('post-detail', pk=self.object.pk)

        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)


class PostSearchView(ListView):
    model = Post
    template_name = 'posts/post_search.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

