#! -*- coding: utf-8 -*-
from os.path import dirname, join
from unittest import TestCase
import pyquery
import pytableparse
import sys

DATA_DIR = join(dirname(__file__), 'data')


def read_file(name):
    f = open(join(DATA_DIR, name))
    c = f.read()
    f.close()
    if sys.version_info[0] == 2:
        return c.decode('utf8')
    return c


class TestPyTable(TestCase):

    def setUp(self):

        content = read_file('1.html')
        table = pyquery.PyQuery(content)('table')
        self.rs = pytableparse.PyTable(table)

        self.keys = ['http://ya.ru', 'http://ya2.ru']
        self.values = [u'Значение1', u'Значение2']

    def test_simply(self):

        self.assertEqual(self.rs.row('key1'), 'value1')
        self.assertEqual(self.rs.row('key2'), 'ya.ru')
        self.assertEqual(self.rs('key2'), 'ya.ru')

    def test_tags(self):

        self.assertEqual(self.rs('key2', '*').html(), '<a href="http://ya.ru">ya.ru</a>')
        self.assertEqual(self.rs('key2', 'a').text(), ['ya.ru'])
        self.assertEqual(self.rs('key2', 'a').text(join=True), 'ya.ru')
        self.assertEqual(self.rs(u'Ключ'), u'Значение1 , Значение2')

    def test_tags2(self):

        keys = ['http://ya.ru', 'http://ya2.ru']
        values = [u'Значение1', u'Значение2']
        self.assertEqual(2, len(self.rs.row(u'Ключ', 'a')))
        for k, v in enumerate(self.rs.row(u'Ключ', 'a')):
            self.assertEqual(v.get('href'), keys[k])
            self.assertEqual(v.text, values[k])

    def test_tags3(self):

        for k, v in enumerate(self.rs.row(u'Ключ', 'a')):
            self.assertEqual(v.get('href'), self.keys[k])
            self.assertEqual(v.text, self.values[k])

    def test_not_exists(self):
        self.assertEqual(self.rs.row(u'dasfasfas'), '')
        self.assertEqual(self.rs.row(u'Ключ', 'span').text(), [])
        self.assertEqual(self.rs.row(u'sadfsaf', 'span').text(), [])
        self.assertEqual(self.rs.row(u'sadfsaf', 'span').asdict(), {})

    def test_tags5(self):

        d = dict(zip(self.keys, self.values))
        self.assertEqual(self.rs.row(u'Ключ', 'a').asdict(), d)


class TestPyTable2(TestCase):

    def setUp(self):

        content = read_file('2.html')
        table = pyquery.PyQuery(content)('.t-row')
        self.rs = pytableparse.PyTable(table)

    def test_simply(self):

        self.assertEqual(self.rs(u'год'), '1968')
        self.assertEqual({u'/country/italiya/': u'Италия'}, self.rs(u'страна', 'a').asdict())

    def test_1(self):

        self.rs(u'в главных ролях', 'a').text()




