import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import streamlit as st
from main import simple_recommender, content_recommendation, improved_recommendation

class TestRecommendation(unittest.TestCase):
    def setUp(self):
        self.books = pd.DataFrame({
            'book_id': [1, 2, 3],
            'title': ['Book1', 'Book2', 'Book3'],
            'authors': ['Author1', 'Author2', 'Author3'],
            'average_rating': [4.5, 4.0, 3.5],
            'ratings_count': [10000, 5000, 2000],
            'content': ['Content1', 'Content2', 'Content3']
        })

    @patch('main.read_book_data')
    def test_simple_recommender(self, mock_read_book_data):
        result = simple_recommender(books=self.books, n=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]['title'], 'Book1')

    @patch('main.read_book_data')
    @patch('main.content', return_value=(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), pd.Series([0, 1, 2], index=['Book1', 'Book2', 'Book3'])))
    def test_content_recommendation(self, mock_read_book_data, mock_content):
        result = content_recommendation(books=self.books, title='Book1', n=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]['title'], 'Book2')

    @patch('main.read_book_data')
    @patch('main.content', return_value=(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), pd.Series([0, 1, 2], index=['Book1', 'Book2', 'Book3'])))
    def test_improved_recommendation(self, mock_read_book_data, mock_content):
        result = improved_recommendation(books=self.books, title='Book1', n=2)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['title'], 'Book2')

if __name__ == '__main__':
    unittest.main()