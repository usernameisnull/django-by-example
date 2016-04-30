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

改进：
1. post_list页面添加了最后一页，和总的项数
6. 添加了发送邮件成功后的返回按钮，返回到post_detail页面

待改进：
   发送邮件的相关配置是明文放在配置里的。