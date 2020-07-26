from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    search,
    resume,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    IndexView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

from projects.views import (
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
)
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    # path('blog/', post_list, name='post-list'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('search/', search, name='search'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    # path('create/', post_create, name='post-create'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    # path('post/<id>/', post_detail, name='post-detail'),
    path('post/<slug>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<id>/update/', post_update, name='post-update'),
    path('post/<slug>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<id>/delete/', post_delete, name='post-delete'),
    path('post/<slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),

    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('project/<slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<slug>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<slug>/delete/', ProjectDeleteView.as_view(), name='post-delete'),
    path('resume/', resume, name='resume'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
