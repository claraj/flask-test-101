from unittest import TestCase  
from unittest.mock import patch
from app import app
from flask import request
import backend

class TestApp(TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        

    @patch('backend.get_animals', side_effect=[ ['cat', 'fish'] ])
    def test_home_page_list(self, mock_list):
        response = self.client.get('/')
        content = response.get_data(as_text=True)
        self.assertEqual(200, response.status_code)
        self.assertIn('cat', content)
        self.assertIn('fish', content)

    
    @patch('backend.get_attributes', side_effect=[ ['example', 'test'] ])
    def test_show_attributes_animal_found(self, mock_get_attr):
        response = self.client.get('/search?animal=cat')
        self.assertEqual(200, response.status_code)
        content = response.get_data(as_text=True)
        self.assertIn('example', content)
        self.assertIn('test', content)


    @patch('backend.get_attributes', side_effect=[ None ])
    def test_show_attributes_404_animal_not_found(self, mock_get_attr):
        response = self.client.get('/search?animal=penguin')
        self.assertEqual(404, response.status_code)
        content = response.get_data(as_text=True)
        self.assertIn('Animal not found', content)
        

    @patch('backend.get_attributes', side_effect=Exception())
    def test_show_attributes_500_connection_error(self, mock_get_attr):
        response = self.client.get('/search?animal=cat')
        self.assertEqual(500, response.status_code)
        content = response.get_data(as_text=True)
        self.assertEqual('Error searching', content)
        


    @patch('backend.like', side_effect=[ True ])
    def test_like_animal(self, mock_like):
        response = self.client.post('/like', data={'animal': 'cat'})
        self.assertEqual(200, response.status_code)
        content = response.get_data(as_text=True)
        self.assertIn('You liked cat!', content)
        

    # no mock because don't expect the like method to be called 
    def test_show_like_no_animal_400_error(self):
        response = self.client.post('/like')
        self.assertEqual(400, response.status_code)
        content = response.get_data(as_text=True)
        self.assertEqual('No animal provided', content)


    @patch('backend.like', side_effect=[None])
    def test_show_like_animal_not_found_error(self, mock_like):
        response = self.client.post('/like', data={'animal': 'penguin'})
        self.assertEqual(404, response.status_code)
        content = response.get_data(as_text=True)
        self.assertEqual('Animal not found', content)


    @patch('backend.like', side_effect=Exception())
    def test_show_like_database_error(self, mock_like):
        response = self.client.post('/like', data={'animal': 'cat'})
        self.assertEqual(500, response.status_code)
        content = response.get_data(as_text=True)
        self.assertEqual('Error saving', content)
        
