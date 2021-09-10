from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Vote, Comment
import datetime

# A function to present the home page
def home(request):

    start_from = datetime.datetime.now() - datetime.timedelta(days=1)
    
    posts = Post.objects.filter(created_at__gte=start_from).order_by('-number_of_votes')[0:30]

    context = {
        'posts':posts
    }

    return render(request, 'HNC_posts/home.html', context)

# A function to submit a post
@login_required
def submit(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('homePage')
    else:
        form = PostForm()
    
    return render(request, 'HNC_posts/submit.html', {'form':form})

# A function to present the detail view of a post
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        return redirect('post', post_id=post_id)
    else:
        form = CommentForm()

    context = {
        'post':post,
        'form':form
    }
    return render(request, 'HNC_posts/detailView.html', context)

# A function to present the votes
@login_required
def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    next_page = request.GET.get('next_page', '')
    
    if post.author != request.user and not Vote.objects.filter(author=request.user, post = post):
        vote = Vote.objects.create(post=post, author=request.user)
    
    if next_page == 'post':
        return redirect('post', post_id=post_id)
    else:
        return redirect('homePage')





