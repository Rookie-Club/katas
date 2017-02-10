import os
import simon
import unittest
import tempfile

class SimonTestCase(unittest.TestCase):

    def setUp(self):
        self.app = simon.app.test_client()

    def test_home_page(self):
        page = self.app.get('/')
        assert b'Welcome to the homepage' in page.data
        assert b'upload' in page.data
        assert b'references' in page.data
        assert b'generate' in page.data

    def test_upload_page(self):
        page = self.app.get('/upload')
        assert b'upload' in page.data
        assert b'<form action="/upload" method="post"' in page.data
        assert b'type="submit"' in page.data

    def test_references_page(self):
        page = self.app.get('/references')
        assert b'references' in page.data

    def test_generate_page(self):
        page = self.app.get('/generate')
        assert b'generate' in page.data

if __name__ == '__main__':
    unittest.main()
