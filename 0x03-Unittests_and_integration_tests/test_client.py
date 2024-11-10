#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class from client.py.
    """

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_result, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct result.
        Ensure no HTTP calls are made and that get_json is called
        once with the expected argument.
        """
        client = GithubOrgClient(org_name)

        mock_get_json.return_value = expected_result

        result = client.org()

        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
