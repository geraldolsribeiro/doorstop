#!/usr/bin/env python

"""
Unit tests for the doorstop.core.item module.
"""

import unittest
from unittest.mock import Mock

import logging

from doorstop.core.item import Item


class MockItem(Item):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._out = ""  # file system mock
        self._read = Mock(side_effect=self._mock_read)
        self._write = Mock(side_effect=self._mock_write)

    def _mock_read(self):
        """Mock read method."""
        text = self._out
        logging.debug("mock read: {0}".format(repr(text)))
        return text

    def _mock_write(self, text):
        """Mock write method"""
        logging.debug("mock write: {0}".format(repr(text)))
        self._out = text


class TestItem(unittest.TestCase):  # pylint: disable=R0904
    """Unit tests for the Item class."""  # pylint: disable=C0103,W0212

    def setUp(self):
        self.item = MockItem('path/to/RQ001.yml')
        self.item._out = "links: []\ntext: ''\nlevel: 1.1.1"

    def test_load_empty(self):
        """Verify loading calls read."""
        self.item.load()
        self.item._read.assert_called_once_with()
        self.assertEqual('', self.item._text)
        self.assertEqual(set(), self.item._links)
        self.assertEqual((1, 1, 1), self.item._level)

    def test_save_empty(self):
        """Verify saving calls write."""
        self.item.save()
        text = "level: '1'\nlinks: []\ntext: ''\n"
        self.item._write.assert_called_once_with(text)

    def test_repr(self):
        """Verify an item can be represented."""
        self.assertEqual(self.item, eval(repr(self.item)))

    def test_str(self):
        """Verify an item can be printed."""
        self.assertEqual('RQ001', str(self.item))

    def test_ne(self):
        """Verify item non-equality is correct."""
        self.assertNotEqual(self.item, None)

    def test_lt(self):
        """Verify items can be compared."""
        item0 = MockItem('path/to/RQ002.yml', level=(1, 1))
        item1 = self.item
        item2 = MockItem('path/to/RQ003.yml', level=(1, 1, 2))
        self.assertLess(item0, item1)
        self.assertLess(item1, item2)
        self.assertGreater(item2, item0)

    def test_id(self):
        """Verify an item's ID can be read but not set."""
        self.assertEqual('RQ001', self.item.id)
        self.assertRaises(AttributeError, setattr, self.item, 'id', 'RQ002')

    def test_prefix(self):
        """Verify an item's prefix can be read but not set."""
        self.assertEqual('RQ', self.item.prefix)
        self.assertRaises(AttributeError, setattr, self.item, 'prefix', 'REQ')

    def test_number(self):
        """Verify an item's number can be read but not set."""
        self.assertEqual(1, self.item.number)
        self.assertRaises(AttributeError, setattr, self.item, 'number', 2)

    def test_level(self):
        """Verify an item's level can be set and read."""
        self.item.level = (1, 2, 3)
        self.assertEqual((1, 2, 3), self.item.level)

    def test_level_from_text(self):
        """Verify an item's level can be set from text and read."""
        self.item.level = "4.2"
        self.assertEqual((4, 2), self.item.level)

    def test_text(self):
        """Verify an item's text can be set and read."""
        self.item.text = "test text"
        self.assertEqual("test text", self.item.text)

    def test_link_add(self):
        """Verify links can be added to an item."""
        self.item.add_link('abc')
        self.item.add_link('123')
        self.assertEqual(['123', 'abc'], self.item.links)

    def test_link_add_duplicate(self):
        """Verify duplicate links are ignored."""
        self.item.add_link('abc')
        self.item.add_link('abc')
        self.assertEqual(['abc'], self.item.links)

    def test_link_remove_duplicate(self):
        """Verify removing a link twice is not an error."""
        self.item.links = ['123', 'abc']
        self.item.remove_link('abc')
        self.item.remove_link('abc')
        self.assertEqual(['123'], self.item.links)


class TestModule(unittest.TestCase):  # pylint: disable=R0904
    """Unit tests for the doorstop.core.item module."""  # pylint: disable=C0103

    def test_tbd(self):
        """Verify TBD."""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
