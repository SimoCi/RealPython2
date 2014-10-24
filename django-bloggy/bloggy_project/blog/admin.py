from django.contrib import admin
from blog.models import Post

# Register your models here.
# tell Django which models you want in the admin area
admin.site.register(Post)
