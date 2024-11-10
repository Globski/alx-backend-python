#!/usr/bin/env python3
import unittest
from unittest.mock import patch
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

@patch('client.get_json')
@patch.object(GithubOrgClient, '_public_repos_url', new_callable=MagicMock)
def test_public_repos_url(self, mock_public_repos_url, mock_get_json):
    """
    Test that the _public_repos_url property returns the correct URL
    based on the mocked org response.
    """
    org_name = "google"
    client = GithubOrgClient(org_name)

    mock_get_json.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

    result = client._public_repos_url

    self.assertEqual(result, "https://api.github.com/orgs/google/repos")
    mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))

@patch('client.get_json')
@patch.object(GithubOrgClient, '_public_repos_url', new_callable=MagicMock)
def test_public_repos(self, mock_public_repos_url, mock_get_json):
    """
    Test that the public_repos method returns the expected list of repos
    and that the mocked methods are called once.
    """
    org_name = "google"
    client = GithubOrgClient(org_name)

    mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
    
    mock_get_json.return_value = [
        {"name": "repo1", "license": {"key": "mit"}},
        {"name": "repo2", "license": {"key": "apache-2.0"}},
    ]

    expected_repos = ["repo1", "repo2"]

    result = client.public_repos()

    self.assertEqual(result, expected_repos)

    mock_get_json.assert_called_once_with(mock_public_repos_url.return_value)
    mock_public_repos_url.assert_called_once()



if __name__ == "__main__":
    unittest.main()
