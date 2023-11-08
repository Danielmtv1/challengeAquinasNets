import unittest
from fastapi.testclient import TestClient
from main import app


class TestWantedEndpoints(unittest.TestCase):
    def setUp(self, state='miami'):
        self.client = TestClient(app)
        post_response = self.client.post(f"/wanted/?state={state}")
        self.assertEqual(post_response.status_code, 200)
        self.post_data = post_response.json()

    def test_get_wanted(self, state='chicago'):
        response = self.client.get(f"/wanted/?state={state}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data) > 0)

    def test_get_wanted_by_id(self):
        response = self.client.get("/wanted/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('name', data)
        self.assertIn('sex', data)
