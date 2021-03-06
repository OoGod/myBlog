from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.
class Tag(models.Model):
	tag_name = models.CharField("标签",max_length=50)

	def __str__(self):
		return self.tag_name 

class Category(models.Model):

	name = models.CharField("文章类型",max_length=50)
	created_time = models.DateTimeField("创建时间",auto_now_add=True)
	last_mod_time = models.DateTimeField("修改时间",auto_now=True)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField("作者姓名",max_length=20)
	avatar = models.ImageField(upload_to='avatar/%Y%m%d',blank=True)
	def __str__(self):
		return self.name

class Article(models.Model):

	title = models.CharField("文章标题",max_length=30)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	content = MDTextField("文章内容")
	djgest = models.TextField("文章概要")
	author = models.ForeignKey(Author,on_delete=models.CASCADE)
	comment_num = models.BigIntegerField(default=0)
	view = models.BigIntegerField(default=0)
	created_time = models.DateTimeField("创建时间",auto_now_add=True)
	last_mod_time = models.DateTimeField("修改时间",auto_now=True)
	tag = models.ManyToManyField(Tag,blank=True)
	def commented(self):

		self.comment_num += 1
		self.save(update_fields=['comment_num'])

	def viewed(self):

		self.view += 1
		self.save(update_fields=['view'])	

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-created_time',)


class Comment(models.Model):
	
	article = models.ForeignKey(Article,on_delete=models.CASCADE)
	content = MDTextField("评论内容")
	author = models.CharField("评论作者",max_length=20)
	email = models.CharField("邮件地址",max_length=30)
	created_time = models.DateTimeField("创建时间",auto_now_add=True)
	last_mod_time = models.DateTimeField("修改时间",auto_now=True)

	class Meta:
		ordering = ('-created_time',)