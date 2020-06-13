from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.urls import reverse
from django import forms
from mdeditor.fields import MDTextFormField
import markdown

from .models import Article, Comment

# Create your views here.
# def  index(request):
	
# 	return HttpResponse("hello!")

def index(request):
	article_list = Article.objects.all()
	paginator = Paginator(article_list,5)
	if request.method == "GET":
		page = request.GET.get('page')
		try:
			books = paginator.page(page)
		except PageNotAnInteger:
			books = paginator.page(1)
		except InvalidPage:
			return HttpResponse("找不到页面")
		except EmptyPage:
			books = paginator.page(paginator.num_pages)
	context = {'article_list': books}
	return render(request,"blog/index.html",context)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		# fields = ('author','email','content',)
		exclude = ('article',)
		# fields = '__all__'
		
		
def detail(request, pk):
	# article = Article.objects.filter(pk=pk)
	article = get_object_or_404(Article,pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.article = article
			post.save()
			article.commented()

		return HttpResponseRedirect(reverse("blog:detail",args=(pk,)))
	comment_list = Comment.objects.filter(article__pk=pk)
	form = CommentForm()
	article.content = markdown.markdown(article.content,
		extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
	context = {'article':article,'comment_list':comment_list,'form':form}
	article.viewed()
	return render(request,"blog/detail.html",context)