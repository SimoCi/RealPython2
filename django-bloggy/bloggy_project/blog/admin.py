from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')

# Register your models here.
# tell Django which models you want in the admin area
admin.site.register(Post, PostAdmin)

