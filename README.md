# 下载到本地
```
git clone https://github.com/OoGod/myBlog.git
```

# 进入MyBlog目录，运行下列命令
```
python install -r requirements.txt
manage.py runserver
```

# 进入后台管理界面
```
manage.py createsuperuser # 创建超用户
```

# heroku部署
```
heroku create # 创建应用程序，可指定程序名
git push heroku master # 部署代码
heroku open # 运行测试
```
