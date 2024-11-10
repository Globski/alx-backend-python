#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from collections.abc import Mapping
from typing import Any, Sequence
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function from utils.py
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that the access_nested_map function correctly accesses nested maps
        and returns the expected values for the given path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises KeyError for missing keys
        and the exception message matches the expected one.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))

if __name__ == "__main__":
    unittest.main()
