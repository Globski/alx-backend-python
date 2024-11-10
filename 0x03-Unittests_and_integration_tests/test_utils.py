#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from collections.abc import Mapping
from typing import Any, Sequence
from utils import (access_nested_map, get_json, memoize)


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises KeyError for missing keys
        and the exception message matches the expected one.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function from utils.py.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json correctly calls requests.get and returns the expected payload.
        """

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator from utils.py.
    """

    class TestClass:
        """
        This class contains a method and a memoized property.
        """

        def a_method(self):
            """
            This method returns 42, which will be memoized.
            """
            return 42

        @memoize
        def a_property(self):
            """
            This is a property that is memoized.
            It calls `a_method` and caches the result.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test that the memoize decorator works as expected.
        Ensure a_method is called only once, even when a_property is accessed multiple times.
        """
        test_instance = self.TestClass()

        with patch.object(test_instance, 'a_method', wraps=test_instance.a_method) as mock_a_method:
            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            mock_a_method.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
