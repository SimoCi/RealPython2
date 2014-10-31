from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Post

######## helper functions #############################################
# helper function to encode urls
def encode_url(url):
	return url.replace(' ', '_')

# helper functions to get 5 most viewd posts
def get_popular_posts():
	return Post.objects.order_by('-views')[:5]

#######################################################################

# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	# retrieve the 5 most viewed posts
	popular_posts = get_popular_posts()

	context_dict = {'latest_posts': latest_posts, 
	'popular_posts': popular_posts}

	# using a for loop to replace the spaces with underscores in a post name
	for post in latest_posts:
		post.url = encode_url(post.title)
	for popular_post in popular_posts:
		popular_post.url = encode_url(popular_post.title)
	t = loader.get_template('blog/index.html')
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, slug):
	# single_post = get_object_or_404(Post, pk=slug)
	single_post = get_object_or_404(Post, 
		title = slug.replace('_', ' '))
	single_post.views += 1 # increment the number of views 
	single_post.save()     # and save it

	# retrieve the 5 most viewed posts
	popular_posts = get_popular_posts()

	context_dict = {'single_post': single_post, 
	'popular_posts': popular_posts}

	for popular_post in popular_posts:
		popular_post.url = encode_url(popular_post.title)

	t = loader.get_template('blog/post.html')
	c = Context(context_dict)
	return HttpResponse(t.render(c))

