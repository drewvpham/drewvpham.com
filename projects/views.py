from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    # form = EmailSignupForm()
    model = Project
    template_name = 'projects.html'
    context_object_name = 'queryset'
    paginate_by = 10

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
        # if self.request.user.is_authenticated:
        #     PostView.objects.get_or_create(
        #         user=self.request.user,
        #         project=obj
        #     )
        return obj

    def get_context_data(self, **kwargs):
        # category_count = get_category_count()
        most_recent = Project.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        # context['category_count'] = category_count
        # context['form'] = self.form
        return context

    # def project(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         project = self.get_object()
    #         form.instance.user = request.user
    #         form.instance.project = project
    #         form.save()
    #         return redirect(reverse("project-detail", kwargs={
    #             'slug': project.slug
    #         }))


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_create.html'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("project-detail", kwargs={
            'slug': form.instance.slug
        }))


def project_update(request, slug):
    title = 'Update'
    project = get_object_or_404(Project, slug=slug)
    form = ProjectForm(
        request.POST or None,
        request.FILES or None,
        instance=project)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("project-detail", kwargs={
                'slug': form.instance.slug
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "project_create.html", context)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/projects'
    template_name = 'project_confirm_delete.html'


def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.delete()
    return redirect(reverse("project-list"))
