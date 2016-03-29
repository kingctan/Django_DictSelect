# Django_DictSelect
使用inclusion_tag标签封装数据字典<br>

最近用java做一个评估系统时，填报系统的前台页面经常用到数据字典（模板标签封装select），于是产生了在django系统下实现这个功能的想法，原理很简单，使用django的inclusion_tag封装select


模板中调用：
---
{% load DictSelect %}<br>
{% DictSelect dictcode='cadeYear' [name='s01'] [id='s01'] [class=''] [value=''] %}<br>
其中方括号为选填。

example：
---
字典：学年 字典编码：cadeYear 字典值：2010-2011 2011-2012 2012-2013 2013-2014 <br>
调用：{% DictSelect dictcode='cadeYear' value='2011-2012' %}<br>
