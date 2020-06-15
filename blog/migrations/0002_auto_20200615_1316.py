# Generated by Django 3.0.7 on 2020-06-15 05:16

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='文章类型')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, verbose_name='标签')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_time',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_time',)},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='djgest',
            field=models.TextField(verbose_name='文章概要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='评论内容'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
