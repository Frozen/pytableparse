#! -*- coding: utf-8 -*-
import six
from pyquery import PyQuery

__all__ = ['PyTable']


class PyTable():

    def __init__(self, pq, value_pos='+', key_el='*'):
        self.table = pq
        self.key_el = key_el
        self.value_pos = value_pos

    def __row(self, text, tag=None):
        rs = self.table(u"{0}".format(self.key_el)).filter(lambda x: PyQuery(this).text() == text)

        val = []
        if self.value_pos == '+':
            val = rs.next()
        if self.value_pos == '-':
            val = rs.prev()

        if not val:
            if tag:
                return EmptyTag()
            return ''

        if not tag:
            return val.text()

        if isinstance(tag, six.string_types):
            return Tag(tag, val)

        raise ValueError

    def __call__(self, *args, **kwargs):
        return self.__row(*args, **kwargs)


class Tag():

    def __init__(self, tag, pyquery_callable):
        self.tag = tag
        self.pyquery_callable = pyquery_callable

    def text(self, join=False, sep=', '):
        ret = []
        for i in self.pyquery_callable(self.tag):
            ret.append(i.text)

        if join:
            return sep.join(ret)
        return ret

    def asdict(self):
        d = {}
        for i in self.pyquery_callable(self.tag):
            d[i.get('href')] = i.text
        return d

    def html(self):
        return self.pyquery_callable(self.tag).html()

    def __iter__(self):
        return iter(self.pyquery_callable(self.tag))

    def __len__(self):
        return len(self.pyquery_callable(self.tag))


class EmptyTag():

    def text(self):
        return []

    def html(self):
        return u''

    def asdict(self):
        return {}

    def __len__(self):
        return 0

