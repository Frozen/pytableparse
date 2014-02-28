pytableparse
============

HTML table key value parsing


```python
from pytableparse import PyTable
from pyquery import PyQuery

table=u"""
<html>
    <head></head>
    <body>
    <table>
        <tr>
            <td>key1</td>
            <td>value1</td>
        </tr>
        <tr>
            <td>Ключ</td>
            <td><a href="http://ya.ru">Значение1</a>, <a href="http://ya2.ru">Значение2</a></td>
        </tr>
    </table>
    </body>
</html>
"""

pt = PyTable(PyQuery(table))

pt('key1')  # 'value1'
pt(u'Ключ')  # u'Значение1 , Значение2'
pt(u'Ключ', 'a').text()  # [u'Значение1', u'Значение2']
pt(u'Ключ', 'span').text()  # []
pt(u'Ключ', 'a').asdict()  # {'http://ya.ru': u'Значение1', 'http://ya2.ru': u'Значение2'}



table=u"""
<div class="row">
   <div class="r-1"><div class="rl-1">название</div><div style="width:185px" class="rl-2 flt">Теорема</div></div>
   <div class="r-1"><div class="rl-1">год</div><div class="rl-2"><a href="/year/1968/" rel="tag">1968</a></div></div>
</div>
"""

pt = PyTable(PyQuery(table))

pt(u'название')  # u'Теорема'
pt(u'год', 'a').asdict()  # {'/year/1968/': u'1968'}

```


