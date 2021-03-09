import unittest

from GithubAPI import queryGithub

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(queryGithub('?'), None)
    def testGithub2(self):
        self.assertEqual(queryGithub('asaltste'), None)
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()