from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

# from .forms import CommentForm, PostForm
from .models import Project


class ProjectListView(ListView):
    # form = EmailSignupForm()
    model = Project
    template_name = 'projects.html'
    context_object_name = 'queryset'
    paginate_by = 1

    # def get_context_data(self, **kwargs):
    #     category_count = get_category_count()
    #     most_recent = Project.objects.order_by('-timestamp')[:3]
    #     context = super().get_context_data(**kwargs)
    #     context['most_recent'] = most_recent
    #     context['page_request_var'] = "page"
    #     context['category_count'] = category_count
    #     context['form'] = self.form
    #     return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(
                user=self.request.user,
                post=obj
            )
        return obj

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))
