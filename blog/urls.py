from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import api , views

 # path('', PostListView.as_view(), name='blog-home'),

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/new/', views.create_post, name='post-create'),
    path('post/<str:slug>/', views.post_detail, name='post-details'),
    # path('post/<str:slug>/', PostDetailView.as_view(), name='post-details'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

    # working with API:
    path('posts/api/', api.post_list_api ,  name='jobs-api'),
    path('posts/api/v2', api.PostListCreateAPIView.as_view() , name='jobs-api-classView'),




]


# ********************************* backup ****

# class PostDetailView(DetailView):
#     model = Post
#     template_name='blog/post_detail.html'
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the Comments
#         post = self.get_object()
#         context['comments'] = post.comments.filter(active=True)
#         context['comment_form'] =CommentForm()


#         return context


# *******************************************
