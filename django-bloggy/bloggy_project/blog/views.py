from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Post

# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	# using a for loop to replace the spaces in a post name with underscores
	for post in latest_posts:
		post.url = post.title.replace(' ', '_') 
	t = loader.get_template('blog/index.html')
	c = Context({'latest_posts': latest_posts, })
	return HttpResponse(t.render(c))

def post(request, slug):
	# single_post = get_object_or_404(Post, pk=slug)
	single_post = get_object_or_404(Post, 
		title = slug.replace('_', ' '))
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post, })
	return HttpResponse(t.render(c))

