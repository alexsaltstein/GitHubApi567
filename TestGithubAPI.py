import unittest
from unittest import mock

import GithubAPI

@mock.patch('GithubAPI.queryGithub')
def mock_query_github(mock_query_github):
    mock_query_github.return_value = []

class TestGithubAPI(unittest.TestCase):
    def testGithubNone(self):
        
        self.assertEqual(GithubAPI.queryGithub('?'), [])
    def testGithubNone2(self):
        self.assertEqual(GithubAPI.queryGithub('asaltste'), [])
    def testGithubSelf(self):
        self.assertEqual(len(GithubAPI.queryGithub('alexsaltstein')), 16)
    def testNoId(self):
        self.assertEqual(GithubAPI.queryGithub(''), [])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()