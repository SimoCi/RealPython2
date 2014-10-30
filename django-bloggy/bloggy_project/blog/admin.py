from django.contrib import admin
from blog.models import Post

# fileds to be displayed in the admin
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'views')

# Register your models here.
# tell Django which models you want in the admin area
admin.site.register(Post, PostAdmin)

