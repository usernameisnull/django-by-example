# django-by-example

django by example 练习的代码
踩坑：
1. 26页的css文件应该放在blog/staic/css/blog.css，书上没有讲到，但是只适用于
   runserver模式下，也就是debug=True。
   http://blog.mymusise.com/?p=170

2. 30页的{% include "pagination.html" with page=posts %}应该为{% include "blog/pagination.html" with page=posts %}
3. 29页的'page': page传进去没用到
4. 在模板里使用了中文，导致UnicodeDecodeError->文件本身使用的编码有问题
5. 41页的cd.to 应该为from.to
6. 50页的new_comment根本没穿进去啊。。
7. models.py里的__str__改为__unicode__，因为我用的python2.7,不然在删除评论的时候会报ascii错误。
8. mark_down自定义过滤器没起作用->不应该忽略那些空行
改进：
1. post_list页面添加了最后一页，和总的项数
6. 添加了发送邮件成功后的返回按钮，返回到post_detail页面

待改进：
   发送邮件的相关配置是明文放在配置里的。
   
问题：
   1. 如何让一个在非pycharm里创建的django工程，用pycharm打开后能识别为django?
      settings->Languages & Frameworks -> Django进行配置
   2. 在添加了评论功能后出现刷新页面出现重复提交，chrome是提示了是否要“确认重新提交表单的”。。。不知道算不算问题
      
      
收获:
    1. 在数据库类中定义了ForeignKey的是多对一的 ‘多’ ，ForeignKey中的related_name是 '一' 这边的 “实例”.related_name
    获得与之相关的“多”这一方的数据的。不能是 OneClass.objects.filter(related_name='xx')这样。
    
    2. forms.ModelForm 
        new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.post = post
        # Save the comment to the database
        new_comment.save()
        # 这样写是因为CommentForm只用了部分的Post的字段，存不进数据库的
        # 这样写也是官方文档的写法
        https://docs.djangoproject.com/en/dev/topics/forms/modelforms/
        
    3.  {% extends xx.html%}应该在模板的第一行
        <ExtendsNode: extends "blog/base.html"> must be the first tag in the template
    
    4.  makemigrations只是在你的model有改变的时候才会起作用，当你把django.contrib.sites和django.contrib.sitemaps
        放在installed_apps里面的时候，直接用migrations