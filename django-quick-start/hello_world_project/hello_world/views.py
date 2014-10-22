from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('<html><body>Hello, world!</body></html>')

def about(request):
	return HttpResponse("Here's the About Page. Want to return home?\
		<href='/'>Back Home</a>")

def better(request):
	t = loader.get_template('betterhello.html')
	c = Context({'current_time': datetime.now(), })
	return HttpResponse(t.render(c))
