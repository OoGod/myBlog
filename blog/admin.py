from django.contrib import admin
# from .models import Article, Author
from .models import Article, Author, Tag, Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)