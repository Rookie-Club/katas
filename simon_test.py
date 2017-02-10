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

    def test_upload_page(self):
        page = self.app.get('/upload')
        self.assertEqual(b'on est sur la page upload', page.data)

    def test_references_page(self):
        page = self.app.get('/references')
        self.assertEqual(b'on est sur la page references', page.data)

    def test_generate_page(self):
        page = self.app.get('/generate')
        self.assertEqual(b'on est sur la page generate', page.data)

if __name__ == '__main__':
    unittest.main()
