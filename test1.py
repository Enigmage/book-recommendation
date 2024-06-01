import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

class TestBookRecommender(unittest.TestCase):

    @patch('main.pd.read_csv')
    def test_read_book_data(self, mock_read_csv):
        # Mocking the return value of pd.read_csv
        mock_read_csv.return_value = pd.DataFrame({
            'book_id': [1, 2],
            'title': ['The Hunger Games (The Hunger Games, #1)', "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)"],
            'authors': ['Suzanne Collins', 'J.K. Rowling'],
            'genres': ['youngadult, fiction, fantasy, sciencefiction, romance', 'fantasy, fiction, youngadult, classics'],
            'description': ['winning means fame and fortunelosing means certain deaththe hunger games have begun   in the ruins of a place once known as north america lies the nation of panem a shining capitol surrounded by twelve outlying districts the capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and once girl between the ages of twelve and eighteen to participate in the annual hunger games a fight to the death on live tvsixteenyearold katniss everdeen regards it as a death sentence when she steps forward to take her sisters place in the games but katniss has been close to dead beforeand survival for her is second nature without really meaning to she becomes a contender but if she is to win she will have to start making choices that weight survival against humanity and life against love', 'harry potters life is miserable his parents are dead and hes stuck with his heartless relatives who force him to live in a tiny closet under the stairs but his fortune changes when he receives a letter that tells him the truth about himself hes a wizard a mysterious visitor rescues him from his relatives and takes him to his new home hogwarts school of witchcraft and wizardryafter a lifetime of bottling up his magical powers harry finally feels like a normal kid but even within the wizarding community he is special he is the boy who lived the only person to have ever survived a killing curse inflicted by the evil lord voldemort who launched a brutal takeover of the wizarding world only to vanish after failing to kill harrythough harrys first year at hogwarts is the best of his life not everything is perfect there is a dangerous secret object hidden within the castle walls and harry believes its his responsibility to prevent it from falling into evil hands but doing so will bring him into contact with forces more terrifying than he ever could have imaginedfull of sympathetic characters wildly imaginative situations and countless exciting details the first installment in the series assembles an unforgettable magical world and sets the stage for many highstakes adventures to come'],
            'average_rating': [4.34, 4.44],
            'ratings_count': [4780653, 4602479],
            'book_counts':[272,491]
        })

        from main import read_book_data
        books = read_book_data()
        self.assertEqual(len(books), 2)
        self.assertEqual(books.iloc[0]['title'], 'The Hunger Games (The Hunger Games, #1)')

    @patch('main.read_book_data')
    def setUp(self, mock_read_book_data):
        # Setting up mock book data
        mock_read_book_data.return_value = pd.DataFrame({
            'book_id': [1, 2],
            'title': ['The Hunger Games (The Hunger Games, #1)', "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)"],
            'authors': ['Suzanne Collins', 'J.K. Rowling'],
            'genres': ['youngadult, fiction, fantasy, sciencefiction, romance', 'fantasy, fiction, youngadult, classics'],
            'description': ['winning means fame and fortunelosing means certain deaththe hunger games have begun   in the ruins of a place once known as north america lies the nation of panem a shining capitol surrounded by twelve outlying districts the capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and once girl between the ages of twelve and eighteen to participate in the annual hunger games a fight to the death on live tvsixteenyearold katniss everdeen regards it as a death sentence when she steps forward to take her sisters place in the games but katniss has been close to dead beforeand survival for her is second nature without really meaning to she becomes a contender but if she is to win she will have to start making choices that weight survival against humanity and life against love', 'harry potters life is miserable his parents are dead and hes stuck with his heartless relatives who force him to live in a tiny closet under the stairs but his fortune changes when he receives a letter that tells him the truth about himself hes a wizard a mysterious visitor rescues him from his relatives and takes him to his new home hogwarts school of witchcraft and wizardryafter a lifetime of bottling up his magical powers harry finally feels like a normal kid but even within the wizarding community he is special he is the boy who lived the only person to have ever survived a killing curse inflicted by the evil lord voldemort who launched a brutal takeover of the wizarding world only to vanish after failing to kill harrythough harrys first year at hogwarts is the best of his life not everything is perfect there is a dangerous secret object hidden within the castle walls and harry believes its his responsibility to prevent it from falling into evil hands but doing so will bring him into contact with forces more terrifying than he ever could have imaginedfull of sympathetic characters wildly imaginative situations and countless exciting details the first installment in the series assembles an unforgettable magical world and sets the stage for many highstakes adventures to come'],
            'average_rating': [4.34, 4.44],
            'ratings_count': [4780653, 4602479],
            'book_counts':[272,491]
        })
        from main import read_book_data
        self.books = read_book_data()

    def test_simple_recommender(self):
        from main import simple_recommender
        recs = simple_recommender(self.books, n=2)
        self.assertEqual(len(recs), 2)
        self.assertIn('The Hunger Games (The Hunger Games, #1)', recs['title'].values)

    # def test_content_recommendation(self):
    #     from main import content_recommendation
    #     recs = content_recommendation(self.books, 'The Hunger Games (The Hunger Games, #1)', n=2)
    #     self.assertEqual(len(recs), 2)
    #     self.assertNotIn('The Hunger Games (The Hunger Games, #1)', recs['title'].values)

    # def test_improved_recommendation(self):
    #     from main import improved_recommendation
    #     recs = improved_recommendation(self.books, 'The Hunger Games (The Hunger Games, #1)', n=3)
    #     self.assertEqual(len(recs), 3)
    #     self.assertNotIn('The Hunger Games (The Hunger Games, #1)', recs['title'].values)


if __name__ == '__main__':
    unittest.main()
