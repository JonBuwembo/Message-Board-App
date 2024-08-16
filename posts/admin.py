from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post

# django is explicitly instructed to display the posts app on the admin page.
admin.site.register(Post)