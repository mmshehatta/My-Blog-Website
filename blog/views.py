from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . forms import PostForm , CommentForm

now = timezone.now()


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post , Comment


def home(request):
    print("*"*100)
    print(now)
    context = {
        'posts': Post.objects.order_by('-id').all(),
        'dateee':now
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted'] we set it i meta class inside post model..god info abassia
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    # def test_func(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     post = Post.objects.get(author=user).first()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostDetailView(DetailView):
    model = Post
    template_name='blog/post_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Comments
        post = self.get_object()
        context['comments'] = post.comments.filter(active=True)


        return context

# ******post_detail function Based View *******
@login_required
def post_detail(request , slug):
    post = get_object_or_404(Post , slug=slug)
    comments = post.comments.filter(active=True)
    if request.method == "POST":
        comment_form = CommentForm(request.POST , request.FILES)
        myform = comment_form.save(commit=False)
        myform.post = post
        comment_form = myform
        print("*********************",myform)
        comment_form.save()
    else:
        comment_form = CommentForm()
    context={
    'title':post,
    'post':post,
    'comment_form':comment_form,
    'comments':comments
    }

    return render(request , 'blog/post_detail.html' , context)




# create new post by using class based view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name='blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# create new Post by function based view


def create_post (request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('blog-home')
    else:
        form = PostForm()

    context={
        'form':form
    }
    return render(request , 'blog/create_post.html' , context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
