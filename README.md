# django-by-example

django by example 练习的代码
踩坑：
1. 26页的css文件应该放在blog/staic/css/blog.css，书上没有讲到，但是只适用于
   runserver模式下，也就是debug=True。
   http://blog.mymusise.com/?p=170

2. 30页的{% include "pagination.html" with page=posts %}应该为{% include "blog/pagination.html" with page=posts %}
3. 29页的'page': page传进去没用到


改进：
1. 添加了最后一页，和总的项数