#!/usr/bin/env python3
"""
Test cases for the utilities in utils.py.

This module contains unit tests for the functions:
- access_nested_map: Tests the access_nested_map function
for correct functionality and exception handling.
- get_json: Tests the get_json function to ensure it correctly
fetches data and handles mock responses.
- memoize: Tests the memoize decorator to ensure that methods
are only called once when their result is cached.
"""
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
        Test that get_json correctly calls requests.get
        and returns the expected payload.
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

    This class tests the functionality of the memoize decorator to ensure
    that it properly caches the results of a method when accessed multiple times.
    """

    class TestClass:
        """
        A test class to demonstrate the use of the memoize decorator.

        This class contains:
        - `a_method`: A method that returns the integer 42.
        - `a_property`: A property that is memoized and calls `a_method` to get its value.
        """
        
        def a_method(self):
            """
            A simple method that returns the integer 42.
            
            This method's result will be cached when called via the memoized `a_property`.
            """
            return 42

        @memoize
        def a_property(self):
            """
            A memoized property that calls `a_method` to get its value.
            
            The result of this property is cached, so subsequent accesses will return
            the cached result instead of recalculating the value by calling `a_method`.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test that the memoize decorator works as expected.

        This test ensures that when the `a_property` is accessed multiple times,
        the underlying `a_method` is only called once, demonstrating that the
        memoize decorator caches the result.

        It also checks that:
        - The method `a_method` is only called once.
        - The result of the `a_property` is correctly memoized and reused.
        """
        test_instance = self.TestClass()

        with patch.object(
            test_instance, 'a_method', wraps=test_instance.a_method
        ) as mock_a_method:
            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            mock_a_method.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
