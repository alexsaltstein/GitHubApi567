import unittest

from GithubAPI import queryGithub

class TestGithubAPI(unittest.TestCase):
    def testGithubNone(self):
        self.assertEqual(queryGithub('?'), [])
    def testGithubNone2(self):
        self.assertEqual(queryGithub('asaltste'), [])
    def testGithubNone2(self):
        self.assertEqual(len(queryGithub('alexsaltstein')), 16)
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()